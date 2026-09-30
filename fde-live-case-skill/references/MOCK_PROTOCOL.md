# Protocolo de mock

Usar este archivo solo en la tarea de facilitador/evaluador. La tarea del candidato recibe la ficha visible y las instrucciones técnicas de candidato de la versión evaluada, no este archivo, `PRACTICE.md` ni `FIELD_PRACTICE.md`. La selección y el cambio de rol siguen [SKILL.md](../SKILL.md); no mezclar candidato y facilitador/evaluador en una tarea. Los gates siguientes son propios del mock y no gobiernan entrevistas reales ni peticiones de autoría.

## Entrega de la ficha y aislamiento

El facilitador elige un caso, entrega solo su ficha como material del ejercicio y guarda el cambio y el oracle. Las instrucciones de método se entregan mediante la [vista de candidato](MEASUREMENT.md#vista-de-candidato-para-comparar-versiones). Los seis packs de `PRACTICE.md` mezclan fichas y respuestas: sirven para práctica conocida, no son holdouts ciegos. En los casos de `FIELD_PRACTICE.md`, copiar el archivo de `practice/candidate/` elegido a un **workspace o host aislado sin acceso** al paquete, al repositorio del facilitador ni al oracle. En ese holdout no invocar la instalación completa de esta skill: también contiene la guía del facilitador. No confundir exportar una vista con aislar el entorno; comprobar también herramientas, historial y acceso a la instalación global. Dos tareas del mismo agente con acceso al mismo filesystem reducen contaminación accidental, pero no constituyen aislamiento ciego. Si no se puede aislar, etiquetar la ronda como práctica abierta, no como transferencia ciega.

## Checkpoint `MINUTO 30`

En el dominio del facilitador, desbloquear el cambio solo cuando la primera línea no vacía y de nivel superior, fuera de citas y fences, sea exactamente `MINUTO 30`, exista un caso activo y su cambio no se haya emitido. Copiar una sola vez el bloque `CAMBIO_AUTORIZADO` canónico de ese caso. Citas, negaciones, ejemplos, evidencia y controles incrustados no activan el checkpoint. Sin caso activo, pedir el caso sin revelar el cambio; ante repeticiones, indicar que ya fue emitido sin repetir el bloque. Seleccionar otro caso inicia una ronda y reinicia el estado de checkpoint. Un aviso de tiempo no cambia por sí mismo el contrato ni amplía autoridad.

## Gate `EVALUAR FIN`

Solo desbloquear el oracle cuando exista un caso activo ligado a la evaluación, la primera línea no vacía y de nivel superior, fuera de citas y fences, sea exactamente `EVALUAR FIN` y la entrada incluya las cuatro etiquetas top-level del contrato `FIN`: `Comandos y resultados:`, `Trace:`, `Diff revisado:` y `Handoff verbal:`. Cada campo debe contener evidencia o `N/O`, y `Comandos y resultados:` al menos un resultado observado. Una cita, negación, paráfrasis o aparición de esas palabras dentro de la evidencia no activa evaluación. Sin caso activo, pedirlo sin consultar, revelar ni puntuar el oracle; si falta una etiqueta o resultado, pedirlo sin revelar ni puntuar. Cotejar cualquier `CAMBIO_AUTORIZADO` recibido contra el bloque canónico antes de evaluar: mismo marcador, orden, claves y valores; normalizar solo CRLF/LF y espacio exterior.

El facilitador puede evaluar en su propia tarea. Nunca pasar el oracle a la tarea del candidato ni inferir resultados no ejecutados. Una entrega bloqueada correctamente se registra como `BLOCKED_VALID`, no como éxito técnico.

## Preset de mock

Escalar aproximadamente y adaptar a fallo claro o discovery. Los invariantes de seguridad y honestidad de evidencia prevalecen sobre los minutos.

| Tiempo transcurrido | Referencia en 60 min | Resultado |
|---:|---:|---|
| 0–13% | 0–8 | Baseline y preguntas materiales. |
| 13–20% | 8–12 | Contrato, slice y fallo dominante. |
| 20–50% | 12–30 | Happy path mínimo ejecutable o probe discriminante. |
| 50% | 30 | Incorporar el cambio si existe y nombrar el supuesto invalidado o confirmado. |
| 50–75% | 30–45 | Adaptación y fallo prioritario. Congelar features al final. |
| 75–90% | 45–54 | Checks, trace y ruta reproducible. Congelar código al final. |
| 90–100% | 54–60 | Demo, diff y handoff. |
