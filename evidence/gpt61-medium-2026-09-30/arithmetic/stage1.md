El total correcto es **2.060 minutos**, no 2.360: el resumen sobreestima la muestra en **300 minutos**.

Cálculo local ejecutado en PowerShell, con salida exitosa:

| Categoría | Operación | Minutos | % del tiempo |
|---|---:|---:|---:|
| Reset | 180 × 3 | 540 | 26,21 % |
| Disputas | 60 × 12 | 720 | 34,95 % |
| Incidentes | 20 × 40 | 800 | 38,83 % |
| **Total** | **540 + 720 + 800** | **2.060** | **100 %** |

Reset tiene el mayor volumen de llamadas, pero **incidentes concentra más tiempo**. Estos datos describen exposición de un día; no demuestran ahorro por automatización ni permiten extrapolar a otros días.

Recomiendo que el responsable de atención revise primero el proceso de incidentes, por su mayor exposición, y contraste qué pasos son abordables en cada categoría. La prioridad de automatización sigue pendiente: requiere conocer elegibilidad, tiempo realmente evitable, esfuerzo y riesgo. Un experimento posterior debería medir ahorro neto frente al proceso actual, incluyendo revisión humana y retrabajo.

No se modificaron archivos ni sistemas externos; no se observaron resultados de automatización.