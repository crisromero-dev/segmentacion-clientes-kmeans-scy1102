# Segmentación de clientes de un centro comercial (K-Means)

Proyecto de la asignatura **SCY1102 Gestión de Proyectos de Datos** (Duoc UC, sección 001D).
**Caso 3 · Retail:** segmentar a 200 clientes de un centro comercial para que marketing decida campañas con evidencia.

**Equipo:** Cristian Romero · Javier Sagredo · Nicolas Osses · Rolando Paredes
**Docente:** Ceferino Sotelo

## Enlaces

| Qué | Enlace |
|---|---|
| Tablero de gestión (Trello) | https://trello.com/b/6GBY0Z0G/segmentacion-de-clientes-scy1102 |
| Dashboard (prototipo, tarea 6.1) | https://segementacion-clientes.netlify.app |
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

1. Instalar dependencias: `pip install pandas numpy scikit-learn matplotlib seaborn openpyxl joblib`
2. Dejar el archivo del caso (`Caso semestral_dataset.xlsx`) en la misma carpeta desde donde se abre el notebook. En Google Colab, el notebook pide subirlo.
3. Ejecutar el notebook de principio a fin. Genera `modelo_segmentacion.joblib`.
4. Reejecución mensual: `python src/segmentacion_mensual.py clientes.xlsx salidas` (el modelo guardado debe estar en la carpeta de trabajo).
5. Dashboard: abrir `dashboard/index.html` en cualquier navegador.

## Datos y privacidad

El dataset del caso **no se incluye** en este repositorio: viene del curso y trae un identificador de cliente sin anonimizar. El script mensual anonimiza el ID con hash y las variables género, edad, educación y estado civil **no entran al modelo**; solo se usan para auditar.

## Nota sobre el seguimiento del proyecto

La parte técnica (modelo, métricas, auditoría y dashboard) se ejecutó sobre el dataset del caso.
El **seguimiento de las semanas 1 a 6** (fechas de ejecución, atraso de Legal, solicitudes de cambio de marketing y costos) es una **simulación** construida sobre el plan aprobado en la evaluación EP3, para ejercitar el monitoreo y control. Está declarada así en el Excel y en el informe.
