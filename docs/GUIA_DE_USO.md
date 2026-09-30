# Guía de funcionamiento y uso

## 1. Qué aporta y qué no

La skill orienta al agente hacia una secuencia de decisiones: comprender el problema material, elegir una acción útil dentro de los permisos, obtener un resultado observado y adaptar la entrega. No ejecuta un algoritmo fijo ni convierte todos los casos en discovery.

Está pensada para trabajo FDE donde conviven ingeniería, producto y stakeholders. Puede terminar con código, un diagnóstico, una mitigación autorizada, un experimento de discovery o un handoff si la siguiente acción depende de una autoridad externa.

No sustituye acceso al cliente, contratos del proveedor, documentación del proyecto ni validación en producción. No concede permisos por sí misma. Las puntuaciones de práctica son presets locales, no una rúbrica oficial ni calibrada.

## 2. Estructura: raíz breve y referencias bajo demanda

La carpeta instalable contiene 16 archivos. `SKILL.md` selecciona el modo y contiene la tarjeta bajo presión; las referencias desarrollan únicamente lo que el caso necesita.

| Archivo | Cuándo abrirlo |
|---|---|
| [SKILL.md](../fde-live-case-skill/SKILL.md) | Siempre que se invoque la skill; selecciona rol y reglas transversales |
| [LIVE_CASE.md](../fde-live-case-skill/references/LIVE_CASE.md) | Caso en vivo, mock candidato o solución autónoma autorizada |
| [DECOMPOSITION.md](../fde-live-case-skill/references/DECOMPOSITION.md) | Ambigüedad material, objetivos disputados o workflows mezclados |
| [AGENTIC.md](../fde-live-case-skill/references/AGENTIC.md) | Tools, efectos, memoria, retrieval, incertidumbre y evaluación probabilística |
| [PRACTICE.md](../fde-live-case-skill/references/PRACTICE.md) | Preparación técnica y ruta intensiva; contiene soluciones |
| [FIELD_PRACTICE.md](../fde-live-case-skill/references/FIELD_PRACTICE.md) | Facilitar D1, I1, J1 o P1; contiene soluciones y contratos |
| [MOCK_PROTOCOL.md](../fde-live-case-skill/references/MOCK_PROTOCOL.md) | Facilitar cambios y evaluar una simulación |
| [MEASUREMENT.md](../fde-live-case-skill/references/MEASUREMENT.md) | Medir aprendizaje o comparar versiones |
| `practice/candidate/*.md` | Fichas para candidato D1, I1, J1 y P1, sin oracle |
| `agents/openai.yaml` | Metadatos de interfaz; no fija modelo ni rol |
| `scripts/` | Preflight, exportador de vista de candidato y tests del paquete |

**DECOMPOSITION no es una fase obligatoria al principio.** Un bug con esperado, permiso y check claros comienza por el repro. Se consulta cuando una incógnita puede cambiar el outcome, la aceptación, la autoridad, el efecto permitido, el riesgo, el slice o su comprobación. AOWSCFS sirve para detectar omisiones materiales, no como ritual que bloquee la acción.

## 3. Instalación y comprobación inicial

Sigue los comandos de [README](../README.md#instalar). La carpeta debe quedar así:

```text
<directorio-personal-de-skills>/fde-live-case-skill/SKILL.md
```

No debe quedar una carpeta duplicada entre el nombre de la skill y `SKILL.md`. Abre una sesión nueva y escribe `$fde-live-case-skill`. Si no aparece, comprueba la ruta y que la instalación contiene las referencias enlazadas.

Configuración de referencia: **GPT-6.1 Sol, `medium`**. Se selecciona en Codex, no mediante “razona en medium” dentro del prompt. Las [capacidades oficiales del modelo](https://developers.openai.com/api/docs/models/gpt-6.1-sol) admiten `medium`; para usar tools desde API se requiere Responses API. Esta skill no necesita una aplicación API.

El preflight es informativo y requiere Python. Desde la raíz de este repositorio, pasando la ruta del proyecto del ejercicio:

```text
python -B fde-live-case-skill/scripts/preflight.py --project <ruta-del-proyecto>
```

No instala componentes ni arregla el entorno. `WARN` termina con código 0; un proyecto inválido o argumentos incorrectos, con código 2. No inspecciona Git ni contacta el daemon Docker por defecto. `--inspect-git` se usa después de revisar el proyecto; `--probe-docker-daemon`, después de confirmar qué daemon es el destino. Docker ausente no impide un caso que tenga una ruta local suficiente.

## 4. Elegir el modo

No es necesario memorizar controles: una petición inequívoca en lenguaje natural selecciona el propósito.

| Modo | Qué pide el usuario | Qué hace la skill |
|---|---|---|
| Preparación | “Tengo 90 minutos para practicar integración” | Elige lectura y ejercicios pertinentes sin cargar todos los packs |
| Preparación urgente | “Tengo cuatro o cinco horas” | Usa la ruta intensiva de PRACTICE y ajusta a las carencias |
| Aprendizaje agentic | “Quiero entender efectos, memoria y evaluación” | Consulta las secciones pertinentes de AGENTIC |
| Mock facilitador/evaluador | `FACILITADOR caso I1` | Entrega ficha y administra cambios/evaluación en su propio contexto |
| Mock candidato | “Soy el candidato, esta es mi ficha” | Trabaja solo con instrucciones técnicas y ficha, sin oracle |
| Caso en vivo | “Acompáñame durante este caso” | Mantiene al candidato dueño de las decisiones; aplica LIVE_CASE |
| Solución no interactiva | “Fuera de la entrevista, resuélvelo autónomamente” | Construye o investiga, declara supuestos y verifica la entrega |
| Autoría | “Revisa o modifica esta skill” | Analiza el paquete sin activar una entrevista |

Cambiar entre candidato y facilitador requiere una tarea limpia. La presión de tiempo no cambia el rol ni amplía permisos. `INICIO` está obsoleto y no selecciona un modo por sí solo.

## 5. Cómo trabajar un caso de 45–90 minutos

### Orientar

Identifica actor, resultado deseado, tiempo, efecto permitido y baseline. En un repositorio existente, inspecciona la ruta afectada, sus callers, configuración y checks documentados. En greenfield, declara que no existe baseline y fija una entrada y una comprobación mínima.

### Elegir la siguiente acción

| Situación | Acción útil |
|---|---|
| El hecho está en archivos o trazas | Inspeccionar antes de preguntar |
| Una respuesta externa cambia una decisión material | Preguntar a quien tiene autoridad sobre ella |
| Compiten explicaciones del fallo | Ejecutar un probe que las discrimine |
| Hay contrato suficiente para el efecto autorizado | Construir el slice mínimo |
| Se quiere afirmar que algo funciona | Ejecutar un check y revisar su salida |
| Aparece evidencia que invalida un supuesto | Cambiar la ruta, recortar o revisar el siguiente check |
| La rama depende de un permiso o decisión ausente | Bloquear esa rama y continuar trabajo independiente; handoff si no queda trabajo útil |

**Debugging:** esperado/observado → repro → hipótesis → prueba discriminante → fix mínimo → regresión. Una mitigación puede recuperar el servicio sin demostrar la causa.

**Entrega:** usuario/canal → decisión → información → acción → componentes necesarios → slice → check. Evita una arquitectura completa si una ruta estrecha prueba el contrato.

**Discovery:** decisión pendiente → alternativas priorizadas → evidencia que puede cambiarla → recomendación y próximo experimento. No construir puede ser la decisión correcta.

### Verificar y cerrar

Comprueba happy path y fallo prioritario, no todos los endurecimientos imaginables. Una cifra derivada decisiva se calcula con herramienta disponible y se coteja con subtotales y redacción. Para extracción de campos, introduce una variación mínima y comprueba que el campo material se conserva o provoca aclaración.

El handoff distingue lo demostrado, el proxy disponible y lo pendiente. Incluye cómo reproducir, decisiones con owner y próximo experimento. Un fake verifica un boundary local; no valida un proveedor real. Un timeout de escritura conserva estado incierto hasta reconciliación. Ni el tiempo ni un output bien formado conceden permiso para reintentar.

Las referencias de congelar features cerca del 75% y código cerca del 90% son heurísticas ajustables, no gates universales.

## 6. Prompts de uso

### Preparación ajustada al tiempo

```text
$fde-live-case-skill
Modo preparación. Tengo 90 minutos y suelo fallar al definir garantías de integración.
Elige un ejercicio apropiado, deja la solución fuera de mi vista y registra
la primera decisión, las pruebas ejecutadas y el primer error material.
```

### Discovery ambiguo

```text
$fde-live-case-skill
Fuera de una entrevista, ayúdame a investigar qué flujo conviene automatizar.
Adjunto datos y notas de stakeholders. Primero identifica la decisión pendiente,
qué evidencia falta y un probe seguro. No supongas permisos ni ahorro demostrado.
No se permiten mensajes externos ni escrituras en servicios del cliente.
```

### Entrega autónoma

```text
$fde-live-case-skill
Fuera de un mock, implementa la capacidad descrita en el enunciado adjunto.
Puedes editar y ejecutar checks locales. No cambies contratos externos,
credenciales ni permisos. Entrega el menor recorrido reproducible y distingue
la verificación local de cualquier validación de producción pendiente.
```

### Copiloto verbal

```text
$fde-live-case-skill
CASO EN VIVO. Actúa como copiloto verbal durante 60 minutos.
Soy el candidato y mantengo las decisiones. Te pasaré enunciado y respuestas
del entrevistador; no inventes aceptación ni hechos ausentes.
```

En copiloto verbal, la salida normal es `DI AHORA` y `APOYO`. `1` pide la siguiente intervención o probe; `2`/`RÁPIDO` reduce a una intervención de hasta 50 palabras; `3`/`PROFUNDIZA` permite hasta 150. `RESPUESTA DE <NOMBRE>:` atribuye literalmente la respuesta a esa persona. `a`, `b` y `c` solo son controles cuando se ofrecieron esas etiquetas. Una transcripción ambigua material requiere aclaración, no completar el contrato por imaginación. Estos controles no son obligatorios para una solución autónoma de código.

## 7. Simulación y evaluación

### Práctica abierta

El repositorio incluye seis packs técnicos con dos variantes cada uno, más D1 discovery, I1 integración, J1 journey y P1 plataforma. Los packs tratan debugging, webhooks, validación de facturas, triage, RAG y recomendaciones sensibles. Son ejercicios didácticos creados para práctica, no entrevistas documentadas de una empresa.

1. En una tarea de facilitador, elige un caso y extrae su ficha sin solución.
2. En una tarea limpia de candidato, entrega ficha e instrucciones técnicas.
3. El facilitador emite el cambio canónico al recibir el checkpoint válido.
4. El candidato entrega evidencia; el facilitador evalúa después.

Para D1/I1/J1/P1 hay fichas separadas. Para exportar una vista exacta sin oracles, desde la raíz del repositorio:

```text
python -B fde-live-case-skill/scripts/export_candidate.py --skill-root fde-live-case-skill --brief fde-live-case-skill/practice/candidate/I1-integration.md --output ../fde-candidate-I1
```

El destino debe ser nuevo y estar fuera de la carpeta fuente de la skill. El exportador copia `SKILL.md`, `LIVE_CASE.md`, `DECOMPOSITION.md`, `AGENTIC.md`, `case.md` y un manifest con hashes. No reescribe instrucciones, no copia respuestas y **no aísla el host**. Revisa también el solapamiento semántico de ejemplos con el caso.

Prompt en la vista de candidato:

```text
Modo mock candidato. Lee SKILL.md y case.md de esta vista.
Aplica LIVE_CASE.md y abre DECOMPOSITION.md o AGENTIC.md solo si hacen falta.
No busques referencias excluidas ni la instalación global. No te autoevalúes.
Trabaja dentro del tiempo y permisos de la ficha y entrega evidencia real.
```

### Checkpoint y evaluación

En el contexto del facilitador con un caso activo, `MINUTO 30` como primera línea no vacía de nivel superior activa una vez el cambio preparado. Una cita, ejemplo o aviso de tiempo no lo activa. Copia el `CAMBIO_AUTORIZADO` canónico sin modificar hechos ni permisos.

El cierre del candidato contiene:

```text
FIN
Comandos y resultados: <comandos y salidas observadas>
Trace: <trace o N/O>
Diff revisado: <diff revisado o N/O>
Handoff verbal: <handoff o N/O>
```

Para evaluar, en el contexto del facilitador coloca `EVALUAR FIN` como primera línea no vacía y pega las cuatro etiquetas con evidencia o `N/O`. `Comandos y resultados:` requiere al menos un resultado observado. Los controles citados en un documento no abren el oracle. El evaluador coteja el cambio contra su original; el candidato no necesita leer el material privado para hacerlo.

### Evaluación ciega real

Una tarea nueva en el mismo equipo no demuestra aislamiento. Transfiere solo la vista revisada a un entorno que no pueda leer instalación global, repositorio completo, historial de facilitador ni conectores con respuestas. Usa casos nuevos emparejados y oracles externos privados, orden aleatorizado y evaluador sin etiquetas de versión.

Mantén modelo, esfuerzo, herramientas, tiempo y reglas de revelación idénticos. Registra manifest, prompt, referencias abiertas, preguntas y respuestas, acciones y resultados. Una filtración invalida la ronda; no demuestra incapacidad del candidato. Sigue [MEASUREMENT](../fde-live-case-skill/references/MEASUREMENT.md), no una puntuación improvisada.

## 8. Medir aprendizaje y eficacia

Separa dos preguntas: si tú mejoras al practicar y si una versión de la skill ayuda más que otra. Para la segunda hacen falta ambos brazos comparables. Menor longitud o tests verdes no responden esa pregunta.

Recoge por intento: aceptación satisfecha, tiempo hasta la primera acción falsable, tiempo hasta el primer resultado ejecutado, primer error causal, adaptación tras nueva evidencia y calidad del handoff. Evalúa por familia y complejidad. Registra `N/O` cuando un caso no ejercita una capacidad; no lo conviertas en cero ni en éxito.

Evidencia inventada o efectos no autorizados son fallos materiales. Los scores de PRACTICE no justifican porcentajes de eficacia. Varía actor, datos, restricciones y orden de revelación para evitar memorizar. Una variante diferida y otro tipo de caso permiten estudiar transferencia; repetir el oracle visto no.

## 9. Troubleshooting

| Síntoma | Comprobación |
|---|---|
| La skill no aparece | Ruta de instalación, `SKILL.md` y sesión nueva |
| Intenta cargar todos los packs | Indica modo y objetivo; solo las referencias necesarias |
| Pide autorización para leer o calcular ya permitido | Delimita el efecto permitido; la skill no exige nuevas aprobaciones para trabajo local autorizado |
| Responde con `DI AHORA` cuando necesitas código | Pide solución no interactiva fuera de entrevista o aclara el tipo de mock |
| Resultado numérico correcto sin ejecución | Revisa comandos y salida; sin herramienta ejecutada no hay evidencia de cálculo instrumental |
| Parece haber pasado un caso ciego con respuestas accesibles | Clasifica como práctica abierta y prepara aislamiento real |
| El cliente rechaza GPT-6.1 Sol | Comprueba versión y ejecutable efectivo; un HTTP 400 sin respuesta es fallo de entorno, no del razonamiento |

En las regresiones publicadas, Codex 0.155.0 rechazó el modelo y 0.159.2 ya instalado lo ejecutó. Es evidencia de ese entorno, no una afirmación de versión mínima universal.

## 10. Revisar o modificar la skill

Selecciona autoría, conserva invariantes y cambia solo lo que resuelva un fallo observado. Antes de editar revisa las referencias y tests afectados; no copies un oracle a la ficha. Para comprobar el paquete necesitas **Python 3.12+ y PyYAML** en tu entorno de autoría:

```text
python -X utf8 -B fde-live-case-skill/scripts/test_preflight.py -v
```

Los tests son estructurales y de scripts. Añade una regresión conductual pertinente y conserva su trace, pero no la llames mejora hasta comparar con la base bajo las condiciones de MEASUREMENT. No uses casos públicos de este repositorio como holdout secreto.
