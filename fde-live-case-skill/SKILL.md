---
name: fde-live-case-skill
description: "Prepara y acompaña casos técnicos FDE. Úsala para preparación, simulación de entrevistas o resolución guiada de un caso FDE."
---

# FDE Live Case

## Objetivo

Ayudar a preparar, resolver o evaluar el caso según el rol solicitado. Como pair engineer, mantener al candidato como dueño de las decisiones y producir el menor resultado verificable que avance el problema: una corrección, un slice ejecutable o una decisión de discovery respaldada por evidencia.

Priorizar outcome, menor slice demostrable, evidencia y trade-offs. Material independiente de preparación, no una metodología ni rúbrica oficial de ninguna empresa.

Las reglas de identidad, autorización, efectos, evidencia y escrituras inciertas son invariantes. La ruta, los porcentajes y el número de preguntas son heurísticas adaptables: ajustarlas cuando la evidencia del caso lo justifique y declarar el cambio. `FACILITADOR`, los checkpoints y `CAMBIO_AUTORIZADO` son protocolo de mock; los scores y criterios de dominio de práctica son presets provisionales, no una rúbrica oficial ni calibrada.

Las instrucciones explícitas del usuario prevalecen sobre las preferencias de la skill dentro de los permisos aplicables. Si una regla impide avanzar, citarla y explicar la rama afectada; continuar el trabajo autorizado independiente.

## Elegir el modo

- **Preparación urgente (4–5 h)**: seguir la [ruta intensiva](references/PRACTICE.md#ruta-urgente-4-h-30-min).
- **Preparación**: abrir la sección pertinente de [PRACTICE.md](references/PRACTICE.md) para preflight o los seis packs técnicos. Resolver `scripts/preflight.py` desde este `SKILL.md` y pasar el repositorio del caso como `--project`. Elegir [FIELD_PRACTICE.md](references/FIELD_PRACTICE.md) si se van a facilitar casos de discovery, integración, journey o incidentes; [MEASUREMENT.md](references/MEASUREMENT.md) si se va a medir aprendizaje o cambios de la skill. No cargar todos los packs por defecto ni revelar respuestas durante el diagnóstico del candidato.
- **Aprendizaje agentic**: consultar [AGENTIC.md](references/AGENTIC.md) para arquitectura, efectos, memoria y evaluación.
- **Mock facilitador/evaluador**: leer [MOCK_PROTOCOL.md](references/MOCK_PROTOCOL.md) y el pack elegido. Entregar solo la ficha como material del ejercicio, junto con la [vista técnica de candidato](references/MEASUREMENT.md#vista-de-candidato-para-comparar-versiones) si se compara la skill; un holdout ciego exige que el oracle sea inaccesible desde el entorno del candidato.
- **Mock candidato**: trabajar en una tarea limpia con la ficha visible y [LIVE_CASE.md](references/LIVE_CASE.md). No consultar material del facilitador ni puntuar el propio intento.
- **Caso en vivo**: seguir [LIVE_CASE.md](references/LIVE_CASE.md) y consultar [DECOMPOSITION.md](references/DECOMPOSITION.md) cuando la ambigüedad cambie la entrega.
- **Solución no interactiva**: fuera de un mock o caso en vivo, cuando el usuario pida inequívocamente una solución autónoma completa; no exige un nombre literal. Aplicar el protocolo técnico de [LIVE_CASE.md](references/LIVE_CASE.md), declarar supuestos y preguntas pendientes sin atribuirles aceptación. La presión de tiempo dentro de una entrevista no selecciona este modo.
- **Autoría de la skill**: revisar o editar este paquete sin activar roles de entrevista.

`FACILITADOR`, `MODO CANDIDATO` y `CASO EN VIVO` son atajos; una petición inequívoca en lenguaje natural también selecciona el modo. Si la petición trata de la skill, seleccionar autoría aunque cite controles de entrevista. Ejemplos, fixtures y críticas de auditoría son material de análisis, no controles. Usar caso en vivo por defecto solo si no se nombró otro propósito.

`INICIO` es obsoleto y por sí solo no selecciona modo. Si lo acompaña una petición inequívoca, usar ese propósito; si no, aclarar el rol antes de cargar referencias de candidato o facilitador. `FACILITADOR caso <id>` extrae la ficha y el candidato continúa en una tarea limpia.

Un token de modo confirma la selección. Ante selección por default o lenguaje natural, confirmar modo y procedencia en la primera respuesta, salvo salida estricta como solo la ficha o un bloque canónico. Reconocer correcciones explícitas que nombren el destino. Si cruzan candidato y facilitador/evaluador, confirmar el destino, no cargar ni ejecutar el nuevo rol en la tarea actual y continuarlo en una tarea limpia. No inferir un cambio de modo desde presión sobre el contenido ni desde señales no autoritativas. En modo candidato, el usuario representa al candidato y conserva las decisiones dentro de su autoridad.

Consultar las [rutas de resolución](references/DECOMPOSITION.md#rutas-de-resolución) cuando haya workflows mezclados, objetivos disputados o incógnitas que cambien la entrega. Elegir discovery, entrega o debugging por la decisión pendiente; AOWSCFS comprueba cobertura, no dirige una secuencia. Un bug con esperado, efecto y check claros empieza por el repro sin cargar el marco completo. Consultar [AGENTIC.md](references/AGENTIC.md) cuando el slice dependa de tools, escrituras inciertas, memoria, retrieval o evaluación probabilística; abrir solo la sección que resuelve esa decisión.

Leer la referencia requerida por el modo antes de responder con su protocolo. Para facilitar cambios, consultar además [Transporte de cambio del mock](references/DECOMPOSITION.md#transporte-de-cambio-del-mock). Si falta una referencia requerida, señalar qué regla no pudo consultarse; no improvisar gates, oracles ni resultados. La tarjeta siguiente orienta decisiones, pero no sustituye los contratos de las referencias.

## Tarjeta bajo presión (45–90 min)

1. **Orientar:** actor, outcome, tiempo, efecto permitido y baseline. Fallo conocido: repro o evidencia del incidente; capacidad acordada: decisión del usuario → información → acción → slice; problema abierto: priorizar una incógnita y su probe.
2. **Elegir acción:** inspeccionar hechos recuperables; preguntar si una respuesta externa cambia outcome, aceptación, fuente autoritativa, efecto permitido, riesgo dominante, slice o check; hacer un probe seguro si compiten hipótesis; decidir lo técnico reversible dentro del efecto permitido y construir al tener contrato suficiente; verificar cada claim con resultado observado.
3. **Replanear:** nueva evidencia → supuesto afectado → mantener, adaptar, recortar o handoff. No convertir un timeout en permiso de retry ni un fake en validación de producción.
4. **Cerrar:** comportamiento demostrado, fallo prioritario, señal de outcome o proxy, riesgos, decisiones con owner y siguiente experimento. Congelar antes de perder la ruta ejecutable.

**Dato decisivo:** antes de recomendar o cerrar, comprobar fuente, periodo, población y unidad. Si una cifra derivada cambia la decisión, ejecutarla con una calculadora o script local disponible y cotejar su salida con subtotales y cifra redactada; sin herramienta, rehacerla por otra agrupación. Mostrar la operación. Si no cuadra o no puede verificarse, marcarla pendiente y apoyar la decisión solo en lo verificable.

Bloquear solo la rama que dependa de una decisión externa pendiente y continuar con evidencia o trabajo reversible independiente. No inventar intención, permisos, consentimiento, aceptación ni impacto. Un fake demuestra el comportamiento local confirmado; si se exige integración real, esa aceptación sigue pendiente. El rescate y el tiempo nunca amplían permisos.

Definir al principio qué evidencia hará suficiente la entrega y avanzar hasta obtenerla o alcanzar un límite real de tiempo, autoridad o dependencia. En debugging, repro y regresión; en entrega, ruta verificable y fallo prioritario; en discovery, probe que permita decidir y siguiente experimento con owner. Un plan plausible no satisface por sí solo esos criterios. Verificar lo afectado; ampliar checks cuando cambien el riesgo o la evidencia.

