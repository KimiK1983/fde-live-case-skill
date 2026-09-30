# Sistemas agentic para casos FDE

## Propósito

Esta guía sirve para decidir, construir y evaluar sistemas que usan modelos para tomar decisiones operativas. No prescribe un framework: el objetivo es elegir la combinación mínima de control que resuelva el problema y conservar autoridad, evidencia y recuperación fuera del modelo.

Para tiempo, roles, autoridad y rescate durante la entrevista prevalecen [SKILL.md](../SKILL.md) y [LIVE_CASE.md](LIVE_CASE.md). Esta guía es la fuente normativa técnica para retries y escrituras inciertas, memoria, retrieval y criterios de adopción; si parecieran competir, el effect envelope, el owner de la decisión y el proceso de la skill mandan.

Material interno del paquete:

- [Decomposition del problema](DECOMPOSITION.md)
- [Mocks cronometrados y seis packs autosuficientes](PRACTICE.md)

## 1. Qué hace agentic a un sistema

Un sistema es agentic cuando el modelo puede elegir la siguiente acción a partir del estado y de observaciones que no conocía al comenzar. Usar un LLM no basta: una extracción, clasificación o redacción aislada es un modelo como componente.

La pregunta útil no es «¿cómo construyo un agente?», sino «¿qué decisión no puedo fijar de forma segura antes de ejecutar?».

### Perfiles de control

Describir el sistema con el perfil o combinación mínima que corresponda; estas etiquetas no forman una progresión obligatoria.

| Perfil | Quién decide la secuencia | Cuándo encaja | Evidencia mínima | Riesgo añadido |
|---|---|---|---|---|
| `D0` — determinista | Código y reglas | El contrato y las decisiones son enumerables | Tests de reglas e invariantes | Complejidad de reglas y casos límite |
| `M1` — modelo como componente | Código; el modelo clasifica, extrae o redacta | Existe ambigüedad semántica, pero no de ejecución | Golden set, schema y validación de negocio | Variación y error semántico |
| `W2` — workflow | Flujo predeterminado con ramas acotadas | La secuencia y los puntos de control son conocidos | Tests por rama, estado y recuperación | Fallos parciales y estado intermedio |
| `A3` — agente acotado | El modelo elige entre tools permitidas hasta un stop | Las observaciones cambian qué acción conviene ejecutar | Evals de trayectoria, budgets y handoff | Loops, tool misuse y efectos indebidos |
| `MA4` — multiagente | Varios agentes coordinan decisiones | Hay ownership, permisos o trabajo paralelo realmente independientes | Evals por agente y del protocolo de coordinación | Más latencia, coste, estados y fallos emergentes |

Estos perfiles son arquetipos pedagógicos de complejidad frecuente, no un orden total de autonomía ni autoridad. Estado, efecto y coordinación son ejes independientes: varios agentes no deben recibir más permisos por ser varios. En una entrevista basta declarar `rol del modelo + control del flujo + efecto máximo`; ampliar el perfil solo si cambia el riesgo o el diseño.

No añadir inferencia, estado dinámico o coordinación por una demo más vistosa. Añadir cada capacidad solo si su baseline más simple falla de forma observable y la alternativa mejora el outcome bajo el mismo conjunto de evaluación.

Un plan, diagrama o diseño plausible no es evidencia de que una causa explique la señal. Mantener hipótesis y alternativas separadas hasta que un repro, intervención o trace las discrimine; el comportamiento observado tampoco prueba intención, disponibilidad ni consentimiento.

Un pipeline puro sigue siendo `D0` mientras una llamada determinista transforme entrada en salida sin estado reanudable. `W2` empieza cuando varias etapas coordinan estado intermedio, ramas, recuperación o handoff explícitos; tener o no un LLM no decide esta frontera.

### Clasificación y readiness

Para clasificar el diseño, responder:

1. ¿Cambiará el siguiente paso según una observación desconocida al inicio?
2. ¿Debe elegir dinámicamente entre acciones permitidas en vez de recorrer ramas predeterminadas?

Si ambas respuestas son afirmativas, el patrón es `A3`; si no, usar `D0`, `M1` o `W2`. La clasificación no demuestra que esté listo para producción.

Antes de desplegar un `A3`, responder además:

3. ¿Las tools, permisos, budgets y condiciones de parada pueden cerrarse?
4. ¿Existe un eval que detecte una trayectoria incorrecta aunque la respuesta final suene bien?

Si alguna respuesta de readiness es «no», reducir el efecto, mantenerlo como prototipo o cerrar ese control; no reclasificar la arquitectura para ocultar la carencia.

## 2. Ciclo seguro de ejecución

```text
input + identidad
        ↓
contexto autorizado + estado vigente
        ↓
decisión propuesta
        ↓
política determinista + aprobación si aplica
        ↓
tool con contrato cerrado
        ↓
resultado validado: applied | failed | unknown
        ↓
estado actualizado
        ↓
stop | siguiente paso dentro del budget | handoff
```

Invariantes:

- La identidad, el tenant y los permisos proceden del sistema, nunca del texto del usuario o del modelo.
- El runtime impone identidad, capabilities, política y budgets; el modelo decide solo dentro de ese envelope. Reglas exactas y efectos sensibles se validan fuera del modelo.
- Una tool vuelve a comprobar autorización y precondiciones en el momento de ejecutarse.
- El contenido recuperado y el resultado de otras tools son datos no confiables, no nuevas instrucciones.
- Todo loop tiene condiciones de parada y budgets antes de empezar.
- Un estado incierto se conserva como `unknown`; no se transforma en éxito ni se reintenta a ciegas.
- El handoff incluye motivo, evidencia, acciones realizadas y estado pendiente.

### Stop y handoff

Parar cuando ocurra la primera condición aplicable:

- outcome alcanzado y verificado;
- falta un dato material que solo una persona puede aportar;
- confianza o evidencia por debajo del umbral;
- siguiente efecto fuera de permisos o pendiente de aprobación;
- resultado de escritura desconocido hasta reconciliar;
- budget de pasos, tiempo, tokens o coste agotado;
- política o fuentes contradictorias.

Un agente que «siempre contesta» suele ocultar fallos. `abstain`, `needs_confirmation`, `pending_reconciliation` y `handoff` son outcomes válidos.

## 3. Contratos de tools y efectos

### Contrato mínimo

Cada tool debe declarar:

| Elemento | Regla |
|---|---|
| Nombre y propósito | Una capacidad estrecha; evitar tools como `execute_anything`. |
| Input | Schema cerrado, tipos, límites y campos desconocidos rechazados. |
| Identidad | `actor_id`, `tenant_id` y scopes inyectados por runtime, no por prompt. |
| Autorización | Comprobación por acción y objeto dentro de la tool. |
| Precondiciones | Versión, estado esperado, límites de negocio y consentimiento vigente. |
| Efecto | `read`, `recommend` o `write`; una tool no debe ocultar un efecto mayor. |
| Timeout y error | Separar `retryable`, `non_retryable` y `unknown`. |
| Idempotencia | Clave estable para la misma intención, conservada en retries. |
| Resultado | Schema validado, estado del efecto y referencia auditable. |

Una salida con JSON válido puede violar una regla de negocio. Validar también invariantes: importe, ownership, transiciones permitidas, evidencia, capacidad y restricciones regulatorias.

Cuando el riesgo lo active, extender el contrato con clase de datos y egress, commit point, concurrencia/versión, consistencia y SLO. Estos campos añaden controles; nunca conceden autoridad.

### Lectura, recomendación y escritura

| Efecto máximo | Control mínimo |
|---|---|
| Lectura | ACL por objeto, minimización de datos y provenance. |
| Recomendación | Evidencia, incertidumbre y responsable humano de la decisión. |
| Escritura reversible | Idempotencia, precondición/versionado, auditoría y compensación o rollback. |
| Escritura sensible o irreversible | Aprobación explícita ligada a argumentos, límites estrictos y handoff cuando cambie el contexto. |

La aprobación debe vincular `actor + acción + argumentos relevantes + versión + caducidad`. «Sí, continúa» no autoriza una operación distinta tras cambiar fecha, importe, destinatario o política.

### Timeout, idempotencia y reconciliación

`retry` resuelve una llamada fallida; idempotencia impide repetir el efecto; reconciliación descubre qué ocurrió cuando la respuesta se perdió. No son intercambiables.

Para una escritura:

1. Validar permiso, precondiciones y argumentos.
2. Derivar una `operation_id` estable de la intención de negocio.
3. Ejecutar con esa clave.
4. Si llega confirmación válida, registrar `applied`.
5. Si hay timeout después de enviar, registrar `unknown` y consultar por `operation_id`.
6. Reintentar solo si la reconciliación confirma que no se aplicó y la operación es segura.
7. Si no puede resolverse, detener y entregar a una persona; nunca inventar estado.

Una saga coordina varios efectos con estados duraderos y compensaciones. La compensación es una nueva acción de negocio, no un borrado mágico: también necesita autorización, idempotencia y evidencia.

### Execution budgets

Definir antes de ejecutar:

- máximo de pasos y llamadas por tool;
- timeout por llamada y deadline total;
- tokens y coste máximos;
- máximo de retries por clase de error;
- volumen máximo leído o devuelto;
- condiciones de parada y handoff.

Al agotar un budget, conservar el estado, emitir `budget_exhausted` y explicar qué falta. No ampliar límites desde el prompt.

### Tool trace mínimo

```text
state_before
→ decision
→ policy_result
→ tool + argumentos relevantes redactados
→ result: applied | failed | unknown
→ state_after
→ stop_reason
```

El trace debe permitir comprobar autorización, orden, duplicados y parada sin guardar secretos, PII innecesaria ni el razonamiento privado del modelo.

## 4. Historial, estado, memoria y retrieval

| Capa | Para qué sirve | Fuente de verdad | Persistencia | Riesgo típico |
|---|---|---|---|---|
| Historial | Dar continuidad a la conversación | Mensajes aceptados | Sesión o retención definida | Prompt injection y PII acumulada |
| Working state | Saber en qué paso está el workflow | Máquina de estados y resultados validados | Hasta terminar o expirar | Saltar una transición o duplicar un efecto |
| Memoria duradera | Reutilizar un hecho estable futuro | Hecho confirmado con provenance | TTL y borrado explícitos | Staleness, poisoning y mezcla de tenants |
| Retrieval | Obtener evidencia externa vigente | Sistema documental o base autorizada | Índice derivado, reconstruible | ACL rota, documentos obsoletos o instrucciones maliciosas |

No usar el transcript como estado operativo. Guardar campos explícitos como `intent`, `missing_fields`, `approved_arguments`, `operation_id`, `effect_status` y `stop_reason`.

Solo escribir memoria cuando el dato:

- sea necesario en futuras sesiones;
- esté confirmado o proceda de una fuente autorizada;
- tenga owner, tenant, provenance, fecha, TTL y mecanismo de corrección/borrado;
- no convierta una inferencia del modelo en hecho.

Ante conflicto, la fuente de verdad gana; la memoria se invalida o marca como obsoleta. Los documentos recuperados no pueden cambiar permisos, políticas ni instrucciones del sistema.

## 5. Threat model agentic

Tratar como fronteras de confianza las capas presentes en el slice: usuario, modelo, memoria, corpus, tools, integraciones y logs. Aplicar los controles correspondientes al efecto real, no implementar toda la tabla por defecto.

| Amenaza | Fallo observable | Control obligatorio |
|---|---|---|
| Prompt injection directa | El texto del usuario intenta sustituir instrucciones, política o permisos | Política fuera del prompt, allowlist de tools y validación determinista. |
| Injection indirecta | Un documento o resultado de tool ordena exfiltrar o actuar | Separar instrucciones de datos, minimizar contexto y no derivar autoridad del contenido. |
| Confused deputy | El agente usa sus privilegios para un objeto ajeno | Identidad del runtime y authz por acción, tenant y objeto dentro de la tool. |
| Acceso cross-tenant | Aparecen datos de otra organización | Namespace, filtros obligatorios, tests negativos y deny by default. El contenido o metadata no autorizados no llegan a contexto, respuesta ni logs; hacer pushdown del ACL cuando sea posible. |
| Exfiltración | Secretos o PII salen por respuesta, tool o log | Minimización, redacción, egress allowlist y logs estructurados sin payload completo. |
| Tool storm o loop | Crecen llamadas, latencia o coste sin progreso | Budgets, detección de no progreso, stop y rate limits. |
| Efecto sin consentimiento | Se ejecuta una acción distinta o caducada | Aprobación ligada a argumentos/versiones y revalidación previa al efecto. |
| Memory poisoning | Una afirmación no verificada reaparece como hecho | Política de escritura, provenance, TTL, revisión y borrado. |
| Resultado ambiguo | Un timeout acaba en efecto duplicado | Estado `unknown`, idempotency key estable y reconciliación. |
| Denial of wallet | Input provoca consumo desproporcionado | Límites de entrada, recuperación y tokens; cuotas por actor/tenant. |
| Credenciales delegadas | Un agente hijo hereda más identidad o scopes de los necesarios | Credenciales efímeras y capabilities reducidas por tarea; la delegación nunca amplía permisos. |
| Tool o código no confiable | Una integración, schema o código recuperado ejecuta instrucciones, secretos o egress inesperados | Pin/review de tools y schemas; sandbox sin secretos ni egress por defecto; validar outputs como datos. |

Pruebas negativas mínimas:

- pedir una tool no permitida;
- solicitar un objeto de otro tenant;
- insertar instrucciones en un documento recuperado;
- cambiar argumentos después de la aprobación;
- provocar timeout después de aplicar una escritura;
- agotar el budget sin progreso;
- intentar persistir como memoria una inferencia no confirmada.

## 6. Evaluar el sistema, no la elocuencia

### Stack de evaluación

| Nivel | Qué comprobar | Ejemplos |
|---|---|---|
| Componente | Contratos y reglas aisladas | Schema, normalización, ACL, cálculo e invariantes. |
| Retrieval | Evidencia correcta y autorizada | Recall de pasajes, citations, freshness, conflictos y abstención. |
| Trayectoria | Decisiones y tools usadas | Tool permitida, argumentos, orden, número de llamadas, no duplicación y stop. |
| Respuesta | Utilidad y grounding | Corrección, cita verificable, incertidumbre y ausencia de afirmaciones sin apoyo. |
| Outcome | Resultado del workflow | Caso resuelto, handoff correcto, efecto único y error recuperable. |
| Seguridad | Comportamiento adversarial | Cross-tenant, injection, PII, consentimiento y budgets. |
| Operación | Calidad de servicio | p50/p95, error rate, tokens, coste, abstención, override y rollback. |

### Golden set útil

Incluir, por segmento relevante:

- happy path;
- dato ausente o ambiguo;
- una variación de un campo material de entrada que no debe perderse durante parsing o normalización;
- resultado válido que viola una regla;
- evidencia insuficiente y contradictoria;
- fallo transitorio antes del efecto;
- timeout después del efecto;
- intento de acceso o instrucción no autorizados;
- caso que debe acabar en abstención o handoff.

Versionar juntos modelo, prompt, schemas/tools, políticas, corpus y conjunto de evaluación. Comparar contra un baseline determinista y repetir casos probabilísticos; informar distribución y peores segmentos, no solo una media.

Definir explícitamente `task`, `trial`, `grader`, `outcome` y versión del harness. Ejecutar trials independientes en entornos limpios cuando el modelo sea parte material de la aceptación. Separar regresiones conocidas de capability/holdouts no vistos; medir tasa de éxito, dispersión y peores segmentos sin llamar “consistencia” a una fórmula no definida.

Un LLM judge puede aportar una señal calibrada contra humanos, pero no debe ser la única autoridad para permisos, dinero, seguridad, citas, duplicados ni reglas verificables por código.

### Criterios de trayectoria

Una respuesta correcta falla si el agente:

- consultó datos no autorizados;
- llamó tools innecesarias o en orden inseguro;
- duplicó una escritura;
- ignoró una contradicción;
- superó budgets;
- omitió el handoff exigido.

Los evals deben comprobar el trace además del texto final.

## 7. Observabilidad, rollout y rollback

Registrar solo lo necesario:

- `correlation_id`, actor/tenant seudonimizados y versión del workflow;
- versiones de modelo, prompt, tools, políticas y corpus;
- decisiones de política, tools llamadas y estados `applied/failed/unknown`;
- pasos, stop reason, handoff, latencia, tokens y coste;
- outcome, abstención, override humano y error clasificado.

Cuando exista una señal disponible, registrar también baseline del proceso, adopción y outcome de negocio o su proxy; no atribuir causalidad al agente sin un diseño de validación.

No registrar transcripts, documentos completos, secretos, PII ni razonamiento privado por defecto. Definir acceso, retención y borrado.

Secuencia de rollout:

1. Replay offline con fixtures y golden set.
2. Shadow mode sin efectos y comparación con el proceso actual.
3. Canary de lectura o recomendación con revisión humana.
4. Escrituras reversibles limitadas, aprobación y kill switch.
5. Ampliación por segmento solo si pasan SLOs, seguridad y outcome.

Rollback significa poder volver a versiones conocidas de modelo, prompt, política, tools y corpus, detener nuevos efectos y reconciliar operaciones `unknown`. Cambiar solo una variable por experimento cuando sea posible.

Alertar por degradación segmentada, no solo global: aumento de handoffs, tools denegadas, loops, latencia, coste, duplicados, accesos cross-tenant o overrides humanos.

## 8. Cuándo no usar cada técnica

| Técnica | No usar cuando | Usar en su lugar | Evidencia para incorporarla |
|---|---|---|---|
| LLM | La decisión es una regla estable y enumerable | Código determinista | El baseline falla por ambigüedad semántica real. |
| Agente `A3` | La secuencia y ramas son conocidas | Workflow `W2` | Observaciones nuevas exigen elegir pasos no fijables de antemano. |
| Multiagente `MA4` | Un solo agente comparte permisos, estado y objetivo | Un agente o funciones normales | Ownership, permisos o paralelismo independientes mejoran un SLO medido. |
| RAG | El contexto autorizado cabe y cambia poco | Contexto completo o lookup exacto | El corpus supera el contexto o exige actualización/provenance. |
| Base vectorial | Se buscan IDs, nombres, códigos o filtros exactos | B-tree, índices de texto, fuzzy o fonética | Las paráfrasis relevantes no se recuperan con búsqueda léxica. |
| Memoria duradera | El dato solo sirve en la sesión | Working state | Reutilización futura justificada con lifecycle y consentimiento. |
| Framework de orquestación | El flujo cabe en funciones y una máquina de estados pequeña | Código normal | Reanudación, espera duradera o ramas observadas justifican su coste. |
| Modelo como juez | La regla puede comprobarse exactamente | Assert, schema o regla | La calidad subjetiva está calibrada contra evaluación humana. |
| Retry | El efecto puede haberse aplicado o el error es permanente | Reconciliación o handoff | Error transitorio y operación probadamente segura/idempotente. |

## 11. Tarjeta verbal de 90 segundos

```text
0–15 s — Actor y outcome
«El actor es __ y necesita __. El resultado observable es __.»

15–30 s — Autonomía
«Elijo reglas deterministas / modelo acotado / workflow / agente porque __.
No aumento autonomía porque __.»

30–48 s — Flujo y efecto
«La entrada validada pasa por __ y la fuente de verdad es __. El sistema puede
leer/recomendar/escribir __; autorización y reglas se comprueban fuera del modelo.»

48–65 s — Fallos y seguridad
«Limito pasos/tiempo/tokens/coste. Ante __ paro y hago handoff. Las escrituras
usan clave estable; un timeout posterior queda unknown hasta reconciliar.»

65–80 s — Evidencia
«Demuestro happy path, fallo dominante y caso adversarial. Evalúo contrato,
tool trace, outcome, seguridad y p95, no solo el texto final.»

80–90 s — Trade-off
«He dejado fuera __ para mantener un slice verificable. Lo añadiría cuando
__ muestre que el baseline actual no cumple __.»
```

La explicación es buena si un entrevistador puede identificar claramente quién conserva la autoridad, qué puede cambiar estado, cómo se detecta el fallo y qué evidencia probará el outcome.
