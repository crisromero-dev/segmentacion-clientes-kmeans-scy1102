# Segmentación de clientes de un centro comercial (K-Means)

Proyecto de la asignatura **SCY1102 Gestión de Proyectos de Datos** (Duoc UC, sección 001D).
**Caso 3 · Retail:** segmentar a 200 clientes de un centro comercial para que marketing decida campañas con evidencia.

**Equipo:** Cristian Romero · Javier Sagredo · Nicolas Osses · Rolando Paredes
**Docente:** Ceferino Sotelo

## Enlaces

| Qué | Enlace |
|---|---|
| Tablero de gestión (Trello) | https://trello.com/b/6GBY0Z0G/segmentacion-de-clientes-scy1102 |
| Notebook en Google Colab | [Abrir en Colab](https://colab.research.google.com/github/USUARIO/segmentacion-clientes-kmeans-scy1102/blob/main/notebooks/Actividad_3_1_2_Implementacion_Tecnica.ipynb) |
| Dashboard (prototipo, tarea 6.1) | PEGAR_AQUI_EL_ENLACE_DE_NETLIFY |
| Repositorio | PEGAR_AQUI_EL_ENLACE_DE_GITHUB |

## Qué hay en el repositorio

| Ruta | Contenido |
|---|---|
| `notebooks/Actividad_3_1_2_Implementacion_Tecnica.ipynb` | Carga y exploración, preparación, división 80/20, elección de k, K-Means con k = 5, métricas, predicciones y auditoría demográfica |
| `src/segmentacion_mensual.py` | Script de reejecución mensual: valida el archivo, asigna segmentos, calcula los controles y emite un reporte de estado |
| `dashboard/index.html` | Prototipo de dashboard (HTML autocontenido, con modo claro y oscuro) |
| `docs/Actividad_3_2_2_Seguimiento_y_Control.xlsx` | Plan, estado, costos (valor ganado), acciones correctivas, riesgos y reporte de avance |
| `docs/Reporte_de_avance_semana_6.pdf` | Reporte de estado al corte de la semana 6 |

## Resultados principales

- **k = 5** sobre ingreso anual y puntaje de gasto (semilla 42).
- Silhouette **0,555** (mínimo del plan: 0,5); Davies-Bouldin 0,57; estabilidad (ARI) 1,00.
- Todos los clientes quedan con segmento (200 de 200).
- La auditoría demográfica detecta **7 alertas** sobre el umbral de 10 puntos porcentuales; por eso un segmento nunca es el único criterio de decisión y cada campaña requiere revisión humana.

## Cómo ejecutarlo

**En Google Colab (forma recomendada)**
1. Abrir el notebook con el enlace "Abrir en Colab" de la tabla de enlaces (o el botón al inicio del notebook).
2. Ejecutar todo: `Entorno de ejecución → Ejecutar todo`. Las librerías ya vienen instaladas en Colab.
3. Cuando el notebook lo pida, subir el archivo del caso (`Caso semestral_dataset.xlsx`).
4. El notebook guarda `modelo_segmentacion.joblib` y crea `segmentacion_mensual.py` en el espacio de trabajo de Colab. Para la reejecución mensual, en una celda nueva: `!python segmentacion_mensual.py "Caso semestral_dataset.xlsx" salidas`

**En local (opcional)**
1. `pip install pandas numpy scikit-learn matplotlib seaborn openpyxl joblib`
2. Dejar el archivo del caso junto al notebook y ejecutarlo de principio a fin.
3. Reejecución mensual: `python src/segmentacion_mensual.py clientes.xlsx salidas` (con `modelo_segmentacion.joblib` en la carpeta de trabajo).

**Dashboard:** abrir `dashboard/index.html` en cualquier navegador, o el enlace publicado.

## Datos y privacidad

El dataset del caso **no se incluye** en este repositorio: viene del curso y trae un identificador de cliente sin anonimizar. El script mensual anonimiza el ID con hash y las variables género, edad, educación y estado civil **no entran al modelo**; solo se usan para auditar.

## Nota sobre el seguimiento del proyecto

La parte técnica (modelo, métricas, auditoría y dashboard) se ejecutó sobre el dataset del caso.
El **seguimiento de las semanas 1 a 6** (fechas de ejecución, atraso de Legal, solicitudes de cambio de marketing y costos) es una **simulación** construida sobre el plan aprobado en la evaluación EP3, para ejercitar el monitoreo y control. Está declarada así en el Excel y en el informe.
