"""Reejecución mensual de la segmentación de clientes (Caso 3 · SCY1102).
Uso:  python segmentacion_mensual.py clientes.xlsx [carpeta_salida]
Programación (ejemplo cron, día 1 de cada mes 07:00):  0 7 1 * *  python segmentacion_mensual.py clientes.xlsx salidas
"""
import sys, os, json, hashlib, datetime as dt
import numpy as np, pandas as pd, joblib
from sklearn.metrics import silhouette_score

UMBRAL_SILHOUETTE = 0.5     # criterio de salida de la fase Modelado
UMBRAL_PP = 10              # auditoría demográfica (RL6)
SAL = os.environ.get('SAL_ANONIMIZACION', 'cambiar-esta-sal-en-produccion')

def limpiar(df):
    df = df.copy(); df.columns = df.columns.str.strip()
    df = df.rename(columns={'Annual Income (k$)': 'Ingreso', 'Spending Score (1-100)': 'Gasto'})
    faltan = {'CustomerID', 'Ingreso', 'Gasto'} - set(df.columns)
    if faltan: raise ValueError(f'Faltan columnas obligatorias: {faltan}')
    for c in ('Education', 'Marital Status'):
        if c in df: df[c] = df[c].replace('Unknown', np.nan)
    df['cliente'] = df.CustomerID.map(lambda i: hashlib.sha256(f'{SAL}-{i}'.encode()).hexdigest()[:10])
    return df.drop(columns='CustomerID')

def auditar(df, variables=('Gender', 'Education', 'Marital Status')):
    alertas = []
    for v in variables:
        if v not in df: continue
        col = df[v].fillna('Unknown'); total = col.value_counts(normalize=True) * 100
        por_seg = pd.crosstab(df['segmento'], col, normalize='index') * 100
        for s in por_seg.index:
            for cat in por_seg.columns:
                dif = por_seg.loc[s, cat] - total[cat]
                if abs(dif) > UMBRAL_PP:
                    alertas.append({'segmento': int(s), 'variable': v, 'categoria': cat, 'diferencia_pp': round(float(dif), 1)})
    return alertas

def ejecutar(ruta_entrada, carpeta_salida='salidas', ruta_modelo='modelo_segmentacion.joblib'):
    os.makedirs(carpeta_salida, exist_ok=True)
    art = joblib.load(ruta_modelo)
    df = limpiar(pd.read_excel(ruta_entrada) if ruta_entrada.endswith('xlsx') else pd.read_csv(ruta_entrada))
    Z = art['escalador'].transform(df[['Ingreso', 'Gasto']])
    df['segmento'] = art['modelo'].predict(Z)
    df['perfil'] = df.segmento.map(art['perfil'])
    sil = float(silhouette_score(Z, df.segmento))
    alertas = auditar(df)
    estado = 'OK' if sil >= UMBRAL_SILHOUETTE and not alertas else 'ALERTA: revisar antes de usar'
    marca = dt.date.today().isoformat()
    df.to_csv(os.path.join(carpeta_salida, f'segmentos_{marca}.csv'), index=False)
    reporte = {'fecha': marca, 'clientes': len(df), 'silhouette': round(sil, 3), 'umbral_silhouette': UMBRAL_SILHOUETTE,
               'tamano_segmentos': {int(k): int(v) for k, v in df.segmento.value_counts().sort_index().items()},
               'alertas_auditoria': alertas, 'estado': estado,
               'nota': 'Revisión humana obligatoria de cada campaña (RL5). No usar los segmentos para excluir ni discriminar.'}
    with open(os.path.join(carpeta_salida, f'reporte_{marca}.json'), 'w', encoding='utf-8') as f:
        json.dump(reporte, f, ensure_ascii=False, indent=2)
    return reporte

if __name__ == '__main__':
    r = ejecutar(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'salidas')
    print(json.dumps(r, ensure_ascii=False, indent=2))