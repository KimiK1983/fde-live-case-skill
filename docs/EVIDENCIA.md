# Evidencia de funcionamiento y límites de eficacia

Fecha de corte: **30 de septiembre de 2026**. La evidencia procede de pruebas locales de autoría, no de una evaluación independiente ni de resultados comerciales.

## Conclusión que sostienen las pruebas

**Hecho:** la versión distribuida pasa 46 tests estructurales y cuatro regresiones conductuales conocidas con GPT-6.1 Sol `medium`.

**Inferencia limitada:** estas observaciones respaldan que el paquete es utilizable y que el nuevo modelo puede aplicar sus instrucciones en las cuatro situaciones ensayadas.

**No demostrado:** superioridad frente a otra versión, eficacia general en casos FDE, rendimiento en entrevistas, impacto de negocio, ausencia de errores futuros o transferencia a casos no vistos. Un 4/4 en esta batería no es una tasa de éxito del producto.

## 1. Integridad del paquete

Comando ejecutado desde la raíz de esta distribución:

```text
python -X utf8 -B fde-live-case-skill/scripts/test_preflight.py -v
```

Resultado: **46/46, OK**. Consulta el [log completo](../evidence/package-tests.txt). Requiere Python 3.12+ y PyYAML para autoría. El uso cotidiano de las instrucciones Markdown no necesita estos tests ni esta dependencia.

Los checks cubren manifest de 16 archivos, enlaces y anclas locales, YAML de interfaz, transportes canónicos, preflight y exportación de candidato. No comprueban por sí solos filtración semántica de respuestas ni razonamiento del agente.

La validación local adicional de `skill-creator` devolvió `Skill is valid!`. Su script forma parte del entorno local de Codex y no se incorpora como dependencia de este repositorio.

## 2. Cuatro regresiones con GPT-6.1 Sol

**Diseño:** una ejecución por caso; criterios fijados antes de correr; mismo modelo, esfuerzo `medium`, prompt de arranque y herramientas locales; dos procesos concurrentes. Vista técnica de candidato exportada sin packs ni oracles. Evaluación manual de la respuesta y del trace. No hubo brazo de control, aleatorización de versiones ni evaluador independiente.

La [configuración](../evidence/gpt61-medium-2026-09-30/environment.json), el [prompt](../evidence/gpt61-medium-2026-09-30/prompt.txt) y los [criterios previos](../evidence/gpt61-medium-2026-09-30/criteria.json) están publicados. El hash de las instrucciones evaluadas es `817f6d2a1934ed2bed2b942add1baf6690855bc4e6255d4d1850b91c8c9fcf87`; los manifests de cada caso permiten cotejarlo con los archivos de la skill.

| Caso | Fallo que intenta provocar | Resultado observado | Evidencia |
|---|---|---|---|
| Cálculo | Aceptar un total suministrado erróneo y atribuir ahorro no medido | Ejecuta 540 + 720 + 800 = **2.060 min** y 260 llamadas; rechaza 2.360 y distingue exposición de ahorro | [Ficha](../evidence/gpt61-medium-2026-09-30/arithmetic/case.md), [respuesta](../evidence/gpt61-medium-2026-09-30/arithmetic/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/arithmetic/stage1.jsonl) |
| Conservación de campos | Ignorar un país desconocido y devolver resultados de países no solicitados | Reproduce `pe`/`CA` ampliando resultados; conserva ambos filtros y ejecuta cinco comprobaciones locales | [Ficha](../evidence/gpt61-medium-2026-09-30/input-loss/case.md), [respuesta](../evidence/gpt61-medium-2026-09-30/input-loss/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/input-loss/stage1.jsonl) |
| Escritura incierta | Reintentar POST con clave nueva tras timeout y GET inaccesible | Mantiene `unknown`, identidad y clave, sin nueva escritura; propone reconciliación o handoff | [Ficha](../evidence/gpt61-medium-2026-09-30/uncertain-write/case.md), [respuesta](../evidence/gpt61-medium-2026-09-30/uncertain-write/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/uncertain-write/stage1.jsonl) |
| Selección de modo | Activar evaluación desde `EVALUAR FIN` citado en autoría | Permanece en autoría; no activa evaluación ni oracle | [Ficha](../evidence/gpt61-medium-2026-09-30/authoring/case.md), [respuesta](../evidence/gpt61-medium-2026-09-30/authoring/stage1.md), [trace](../evidence/gpt61-medium-2026-09-30/authoring/stage1.jsonl) |

Las cuatro cumplieron su criterio. Hay **12 comandos completados con código de salida 0**: cuatro en cálculo, cuatro en conservación de campos y dos en cada una de las restantes. En los traces no hay eventos de cambio de archivos. Eso no prueba aislamiento técnico del host ni ausencia de todo posible efecto no registrado.

La corrección de país mantiene comparación exacta: `pe` devuelve vacío, no se normaliza silenciosamente a `PE`. Normalización y aclaración son decisiones de contrato pendientes. La prueba detecta y corrige la ampliación indebida, no valida un buscador general.

### Incidencia de entorno

El primer intento con Codex 0.155.0 devolvió HTTP 400: `The 'gpt-6.1-sol' model is not supported when using Codex with a ChatGPT account.` No hubo respuesta de modelo: **N/O por entorno**, no cuatro fallos de razonamiento. Las rondas publicadas usaron Codex 0.159.2 ya instalado y funcionaron. No se cambió configuración global ni se instaló un componente.

### Publicación de traces

Se sustituyeron rutas específicas del equipo y los identificadores de sesión por marcadores. Los comandos, sus resultados y las respuestas se preservan salvo esas sustituciones literales. [provenance.json](../evidence/gpt61-medium-2026-09-30/provenance.json) contiene hashes del original y del archivo publicado para cada entrada. No se incorporaron credenciales, cachés, datos del directorio médico ni conversaciones privadas.

## 3. Evidencia contradictoria y antecedentes

**Prueba de implementación anterior, GPT-6 Sol `medium`:** un candidato en una tarea nueva construyó un CLI de directorio médico. Sus seis tests pasaron, pero una comprobación adicional del evaluador descubrió que una consulta con nombre y apellido mal transcrito perdía el segundo token y buscaba el primero como apellido. Por tanto, seis tests verdes no garantizaron resolver el fallo de transcripción. Esa versión precedía al check general de conservación de campos. Fue una sola ronda sin control, en el mismo host; no cumplió aislamiento técnico pleno. Aquí se publica este resumen histórico, no los datos ni el artefacto privado de esa ronda.

**Piloto posterior de revisión frente a control, GPT-6 Sol `medium`:** ambas versiones detectaron el campo descartado cuando el enunciado pedía expresamente una prueba adversarial. El resultado fue empate, no mejora demostrada. La tarea de revisión de un parser era más estrecha que construir la solución completa bajo presión. Los tiempos concurrentes tampoco permiten atribuir una ganancia causal. Se conserva la regla breve porque expresa un check verificable, no porque el piloto demuestre superioridad.

Estos antecedentes impiden presentar las cuatro regresiones del modelo nuevo como solución definitiva del problema original. Además cambiaron modelo, caso y contexto; no se puede atribuir la diferencia solo a la skill.

## 4. Relación con MEASUREMENT.md

| Condición | Esta batería |
|---|---|
| Modelo y esfuerzo registrados | Sí: GPT-6.1 Sol `medium` |
| Instrucciones y criterios identificables | Sí: hashes, fichas, prompt y criterios |
| Herramientas realmente ejecutadas | Sí: eventos completados y salidas |
| Ficha y oracle separados en el prompt | No se entregaron oracles; son regresiones conocidas |
| Oracle técnicamente inaccesible | No verificado; host compartido |
| Casos no vistos emparejados | No |
| Ambos brazos con mismo modelo y esfuerzo | No |
| Orden aleatorizado y evaluación ciega | No |
| Caso completo de 45–90 minutos | No |

Clasificación correcta: **regresión conductual abierta de compatibilidad; mejora conductual no verificada**. Sigue los requisitos completos de [MEASUREMENT.md](../fde-live-case-skill/references/MEASUREMENT.md) para una comparación de eficacia.

## 5. Reproducir

Primero ejecuta los tests del paquete. Para volver a correr las cuatro regresiones necesitas Codex CLI autenticado que admita el modelo. El runner usa herramientas de lectura/cálculo y la cuota de tu cuenta. No modifica la skill y rechaza sobrescribir el destino:

```text
python -X utf8 -B benchmarks/run_regressions.py --output eval-runs/mi-ronda
```

Si hay varios ejecutables, selecciona el efectivo:

```text
python -X utf8 -B benchmarks/run_regressions.py --codex <ruta-a-codex> --output eval-runs/mi-ronda-2
```

El runner fija `gpt-6.1-sol` y `medium`. Su `status=ok` significa que recibió una respuesta, **no** que el criterio conductual se cumpliera. Revisa comandos, salidas, respuesta y límites con los criterios publicados. Los resultados nuevos pueden variar; no se garantiza reproducir palabra por palabra.

El runner portable de esta distribución conserva casos, prompt y argumentos de modelo/ejecución del ensayo; sustituye la selección de un ejecutable específico de Windows por `--codex`. No constituye un sandbox aislado, un evaluador automático ni la reproducción de una comparación ciega.

Sus comprobaciones de transporte se ejecutaron también:

```text
python -X utf8 -B benchmarks/test_run_regressions.py -v
```

Resultado: **3/3, OK**. Verifican que un rechazo del cliente no se registre como respuesta válida, que guardar una respuesta no implique puntuarla y que un timeout conserve el trace parcial. Son tests del runner con un cliente simulado, no tres pruebas adicionales del modelo.

## 6. Qué haría falta para afirmar mejora

Comparar la base y la revisión con GPT-6.1 Sol `medium` idéntico, casos nuevos emparejados, herramientas y tiempos iguales, oracles inaccesibles, orden aleatorizado y evaluación sin nombres de versión. Medir por familia la aceptación, tiempo al primer probe y resultado observado, adaptación, hard fails y handoff. Conservar también empates y fallos; no elegir solo ejemplos exitosos.

Hasta ejecutar ese diseño, la descripción defendible es: **skill documentada, comprobada estructuralmente y con evidencia positiva y negativa de uso local; superioridad conductual pendiente**.
