# Casos FDE de transferencia: guía del facilitador

Estos cuatro casos son ejercicios didácticos creados para practicar capacidades menos cubiertas por los seis packs técnicos de `PRACTICE.md`; no son entrevistas documentadas ni datos de clientes. Entregar al candidato **solo** el archivo correspondiente de `practice/candidate/` como material del ejercicio, junto con las instrucciones técnicas permitidas según [MEASUREMENT.md](MEASUREMENT.md#vista-de-candidato-para-comparar-versiones). Mantener esta guía fuera de su entorno para una ronda ciega. Usar [MOCK_PROTOCOL.md](MOCK_PROTOCOL.md) para el cambio y la evaluación; [MEASUREMENT.md](MEASUREMENT.md) para el registro. Los criterios siguientes son observables de práctica, no rúbrica oficial.

| Caso | Ficha visible | Qué prueba |
|---|---|---|
| D1 | [Discovery y priorización](../practice/candidate/D1-discovery.md) | Discovery con actores, outcome y no-construcción justificable. |
| I1 | [Integración empresarial](../practice/candidate/I1-integration.md) | Semántica de escritura incierta y límite de permisos. |
| J1 | [Journey conversacional](../practice/candidate/J1-journey.md) | Estado de conversación, corrección y métrica de negocio. |
| P1 | [Incidente de plataforma](../practice/candidate/P1-platform.md) | Diagnóstico de latencia y decisión cliente/plataforma. |

## D1 — Discovery y priorización

**Oracle del facilitador.** La petición “automatizar 80% de llamadas” no fija un outcome ni autoriza escrituras. Esperar preguntas al sponsor de operaciones y a dueños de proceso: coste/tiempo actual, errores, abandono, seguridad, quién acepta el piloto y qué sistemas son fuente de verdad. Del cuadro disponible, volumen × duración da 600, 900, 960 y 240 min/día respectivamente; eso estima exposición de tiempo, no ahorro causal ni prioridad definitiva. Una opción defendible es cambios de cita por volumen y API sandbox, con piloto humano supervisado, baseline de resolución correcta/tiempo/handoff, propietario y stop; otra también puede pasar si sus límites están explícitos. Billing disputes es lectura, no resolución autorizada; safety reports exigen humano. No premiar una arquitectura antes de decidir problema y efecto.

**Cambio al 50%.** El equipo de IT confirma que la API de agenda no tiene scope de escritura en producción y el proveedor aún no da fecha. Entregar exactamente:

```text
CAMBIO_AUTORIZADO
caso: D1
checkpoint: 50%
tipo: confirma
incógnita: ¿Se puede escribir en la agenda de producción?
alcance: piloto de cambios de cita
decisión: Solo lectura/simulación hasta permiso explícito.
```

No autoriza fabricar el permiso. **Observables:** reformula outcome, cuantifica solo lo que los datos permiten, escoge un probe que discrimina, contiene la rama write, propone decisión y dueño siguiente. **Fallo prioritario:** prometer deflexión o ahorro, o implementar cambio real sin permiso. **Handoff:** qué se midió, qué no, quién habilita scope y cómo validar el piloto.

## I1 — Integración empresarial

**Oracle del facilitador.** Tras timeout de POST, el estado es `unknown`; antes de retry, consultar GET por `operation_id` si hay permiso. Con GET=`applied`, no repetir; con GET=`not_found` autoritativo y la garantía vigente descrita en la ficha, retry con la misma key y payload, conservando permiso y precondiciones; con GET inaccesible, handoff/pendiente. Un fake local puede demostrar estas ramas, pero no valida scopes ni comportamiento real del proveedor. Exigir key estable, estados explícitos y evidencia de que una intención no produce dos tickets. No sugerir elevar permisos. Las respuestas del facilitador deben reproducir el contrato del fake de la ficha, no inventar otra retención, consistencia o alcance de clave. Si esas condiciones no están confirmadas en una variante, aceptar `unknown` y handoff como bloqueo válido; no exigir retry para aprobar. Probar también rechazo de misma clave con payload distinto y deduplicación concurrente si la implementación afirma esa garantía.

**Cambio al 50%.** El service principal de producción carece también de scope GET para consultar operaciones. Entregar exactamente:

```text
CAMBIO_AUTORIZADO
caso: I1
checkpoint: 50%
tipo: confirma
incógnita: ¿Se puede reconciliar el resultado real?
alcance: reconciliación real
decisión: Bloquear retry real y comunicar a IT la falta de permiso GET; el candidato no modifica scopes, su autorización y habilitación corresponden a IT. Fake local permitido solo como prueba interna.
```

**Observables:** boundary pequeño, prueba del timeout-aplicado y del bloqueo sin GET, claim exacta del fake, dueño del permiso. **Fallo prioritario:** retry ciego o claim de integración validada solo por fake.

## J1 — Journey conversacional

**Oracle del facilitador.** La secuencia mínima tiene datos de vehículo, cotización vigente ligada a esos datos, confirmación y solicitud de cita. Una corrección material de versión/trim invalida cotización y confirmación anteriores; el sistema debe volver a cotizar o hacer handoff, no reservar con precio stale. Métrica primaria propuesta: citas válidas completadas o aprobadas por humano por cohorte; proxies: tasa de cotización válida, correcciones recuperadas, handoff, abandono, latencia. Containment por sí solo puede empeorar el outcome. Falso positivo: una demo que repite el flujo feliz sin prueba de corrección.

**Cambio al 50%.** El usuario ya aceptó la cotización q1 para los datos v1; antes de confirmar una cita, corrige el trim y los datos pasan a v2. Entregar exactamente:

```text
CAMBIO_AUTORIZADO
caso: J1
checkpoint: 50%
tipo: confirma
incógnita: ¿Sigue vigente la cotización anterior?
alcance: cotización y confirmación de cita
decisión: El usuario aceptó q1 para datos v1 y ahora corrige el trim a v2, antes de confirmar una cita. Invalidar q1 y su aceptación; recotizar o hacer handoff, y obtener nueva aceptación antes de continuar. Ninguna reserva real está autorizada.
```

**Variantes locales de cobertura:** (a) corrección tras precio pero antes de aceptación: q1 deja de ser utilizable; (b) datos v1 → q1 → aceptación q1 → corrección material v2: ni q1 ni su aceptación sirven para avanzar, incluso si q2 tiene el mismo precio. Una nueva cotización no hereda el consentimiento anterior. La cita solo puede avanzar localmente con aceptación vigente y confirmación específica, sin efecto externo. Registrar ambas variantes por separado; recotizar no demuestra por sí solo invalidación de aceptación.

**Observables:** estado/versionado o regla equivalente, prueba de invalidación de cotización y aceptación ya concedida, consentimiento/efecto antes de booking, medición de calidad y handoff. **Fallo prioritario:** reservar con precio o aprobación anterior.

## P1 — Incidente de plataforma

**Oracle del facilitador.** La tabla de trazas solo permite hipótesis, no p95 de producción ni causalidad. Comparar segmentos, correlacionar concurrencia con cola del orquestador, pedir/probar un perfil acotado o trace adicional read-only y aislar el cuello antes de cambiar timeout. Mantener workaround del cliente separado del fix compartido, con owner de plataforma, rollout y rollback. La evidencia de un segundo cliente cambia prioridad de generalización, no demuestra una causa única.

**Cambio al 50%.** Un segundo cliente presenta el mismo aumento de latencia en la etapa de cola con concurrencia similar. Entregar exactamente:

```text
CAMBIO_AUTORIZADO
caso: P1
checkpoint: 50%
tipo: confirma
incógnita: ¿El cuello pertenece a la plataforma compartida?
alcance: triage de plataforma
decisión: Un segundo cliente presenta aumento de latencia en la etapa de cola con concurrencia similar. Investigar la hipótesis de un cuello compartido, sin darla por demostrada; mantener la mitigación por cliente limitada a análisis o pruebas locales/read-only, sin cambios reales de timeout, escala o configuración.
```

**Observables:** probe discriminante, comparación antes/después y por segmento, contención sin esconder error, handoff con hipótesis frente a hechos. **Fallo prioritario:** subir timeouts y afirmar que se resolvió sin medir.
