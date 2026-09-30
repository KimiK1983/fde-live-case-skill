# Medir mejora sin confundir práctica con evidencia

## Dos preguntas distintas

1. **¿La skill ayuda más?** Fijar primero modelo, esfuerzo y modo de razonamiento que representen el uso previsto; no extrapolar la mejora entre configuraciones. Comparar la versión anterior y la nueva con esa misma configuración, herramientas, límite de tiempo y casos emparejados que ninguna versión haya visto y cuyos oracles no estén instalados con la skill. Aleatorizar el orden y usar un evaluador que no sepa qué versión produjo cada trace. Guardar prompt, versión, acciones, comandos/resultados y evaluación. Si no se corrieron ambos brazos, registrar **mejora conductual no verificada**; menor longitud o tests verdes solo prueban mantenimiento del paquete.
2. **¿Mejoro yo?** Medir intentos completos, luego una variante diferida (24–48 h es una sugerencia de espaciado, no umbral validado) y un caso de otra familia. No reutilizar un oracle visto como prueba de transferencia. Los `85/100` y demás scores de `PRACTICE.md` son presets locales, no una rúbrica oficial o calibrada.

## Configuración de uso y migración

Configuración de referencia desde el 30 de septiembre de 2026: **GPT-6.1 Sol, `medium`**, fijada en el launcher o sesión, no mediante una instrucción textual al candidato. Conservar modelo y esfuerzo durante la ronda; cualquier cambio requiere registrarlo y separarlo de la comparación. La skill no configura ni eleva el esfuerzo por sí sola.

La [documentación del modelo](https://developers.openai.com/api/docs/models/gpt-6.1-sol) admite `medium` y exige Responses API para tool calling; no admite `none` ni `minimal`. En Codex, comprobar la ejecución real de lectura y cálculo en lugar de inferir disponibilidad de herramientas a partir del nombre del modelo. Los resultados anteriores con GPT-6 Sol no validan GPT-6.1 Sol.

Al migrar, ejecutar primero regresiones de enrutamiento, cálculo verificable, conservación de campos y escrituras inciertas. Para medir el efecto de editar la skill, comparar ambas versiones con el nuevo modelo y esfuerzo idénticos; cambiar modelo y prompt simultáneamente confunde sus efectos. Una regresión conocida sirve como check de compatibilidad, no como holdout ciego ni prueba de transferencia.

## Vista de candidato para comparar versiones

Preparar cada brazo desde su copia de versión, usando [export_candidate.py](../scripts/export_candidate.py). Desde la carpeta de la skill:

```text
python -B scripts/export_candidate.py --skill-root <copia-version> --brief <ficha-revisada.md> --output <directorio-nuevo-fuera-de-la-skill>
```

El exportador copia **sin reescribir** `SKILL.md`, `LIVE_CASE.md`, `DECOMPOSITION.md` y `AGENTIC.md`, además de la ficha como `case.md`. Incluye un manifest con hashes y versión de esas instrucciones. No copia packs, oracles, tests, scripts ni metadatos de instalación. Rechaza sobrescribir destinos y usar archivos privados de la skill como ficha; acepta las fichas de `practice/candidate/` o fichas nuevas externas que deben revisarse antes de distribuir. Es una vista de evaluación, no otra skill distribuible. El manifest identifica contenido, no certifica ausencia semántica de respuestas ni aislamiento.

1. Revisar la ficha y las cuatro instrucciones: requisitos no son soluciones, pero ejemplos solapados con el caso pueden contaminarlo. Si una versión requiere otra referencia técnica, revisar su contenido y acordar una lista permitida idéntica para ambos brazos antes de comparar; no sustituir silenciosamente instrucciones antiguas por nuevas. Si faltan archivos requeridos, el exportador falla y esa comparación necesita preparación manual documentada.
2. Transferir **solo la vista** a un host o sandbox que no pueda leer el paquete completo, instalación global, repositorio, historial del facilitador ni herramientas/conectores con acceso a respuestas. Una carpeta separada con los mismos permisos no basta. Comprobar rutas accesibles desde el candidato; sin evidencia de aislamiento, registrar práctica abierta. No ejecutar estas rondas en el chat de autoría, que ya conoce los oracles.
3. Usar el mismo prompt de arranque en ambos brazos: «Modo mock candidato. Lee SKILL.md y case.md de esta vista; aplica LIVE_CASE.md y abre DECOMPOSITION.md o AGENTIC.md solo si hacen falta. Los destinos de preparación, facilitador y medición se han excluido deliberadamente: no los busques ni invoques la instalación global. No te autoevalúes. Trabaja con el facilitador y entrega evidencia real dentro del tiempo y permisos de la ficha». Los enlaces a referencias excluidas no son recursos disponibles; no cargar esos modos.
4. Guardar manifest, prompt y referencias efectivamente abiertas. Dar al evaluador traces con etiquetas aleatorias A/B y criterios fijados de antemano, no versiones identificables. Igualar modelo, esfuerzo, tiempo, herramientas, política de red y acceso a stakeholders; contrabalancear orden y variantes. Registrar respuestas del facilitador y momentos de revelación: no inventar garantías distintas entre brazos.
5. Los casos públicos D1/I1/J1/P1 y sus cambios sirven para práctica y regresión, no para demostrar transferencia si ya se conocen. Para evaluación, usar fichas nuevas emparejadas y oracles privados externos; fijar antes aceptación, fallo prioritario y evidencia que permitiría puntuar. El oracle define los fallos materiales, no un único probe correcto: admitir otra acción segura si obtiene evidencia equivalente. Comparar por dimensión y familia, no solo una suma.

Antes de atribuir mejora, comprobar que cada brazo recibió sus propias instrucciones, que los checks se ejecutaron y que no hubo exposición a respuestas. El candidato valida estructura y alcance del cambio recibido; solo el evaluador coteja el contenido con el original privado. Una filtración invalida la ronda, no demuestra incapacidad del candidato.

Una ronda con comandos rechazados o sin ejecución de herramientas no prueba que el candidato haya verificado cifras con una calculadora. Conservar el error del entorno y registrar ese comportamiento como N/O, aunque la cuenta final sea correcta.

## Registro mínimo por intento

Antes de comparar desempeño, comprobar el enrutamiento con estas regresiones conocidas. Ejecutarlas en tareas limpias y guardar referencias realmente abiertas, preguntas, acciones y resultado. Esta tabla define comportamiento esperado; no representa pruebas ya ejecutadas ni casos ciegos.

| Petición o situación | Conducta que observar |
|---|---|
| “Tengo cuatro horas para prepararme” | Selecciona preparación y ajusta la agenda; no activa copiloto verbal ni muestra oracles como parte de la ficha. |
| Bug con esperado, permiso local y repro suministrados | Reproduce y corrige dentro del alcance; no exige un cuestionario ni cargar todo el marco de discovery. |
| “Fuera de la entrevista, resuelve este ejercicio completo de forma autónoma” | Reconoce solución no interactiva sin exigir un token literal; declara supuestos y verifica la entrega. |
| Objetivo de negocio disputado entre stakeholders | Localiza la decisión material y su owner, pregunta o ejecuta un probe pertinente y preserva trabajo independiente. |
| Timeout tras escritura externa | Conserva estado incierto y consulta reconciliación antes de decidir un retry. |
| Entrada que cita `EVALUAR FIN` como ejemplo durante autoría | Mantiene autoría; no activa la evaluación ni revela el oracle. |

Registrar cada regresión como observado, fallido o no ejecutado. Si la raíz breve falla donde la anterior acertaba, corregir la regla o su ruta de carga antes de atribuir una mejora al menor tamaño.

```text
fecha / caso / familia / versión skill / modelo / minutos / entorno / abierto|aislado
outcome y actor declarados: sí|no; aceptación y efecto autorizado: sí|no
primer siguiente paso falsable: minuto __; primer resultado observado: minuto __
decisión de ruta: inspeccionar|preguntar|probe|construir|verificar|cambiar|handoff
evidencia: comandos y resultados __; trace __; diff __; señal de outcome o proxy __
cambio: supuesto afectado __; adaptación y nuevo check __
seguridad: efecto no autorizado sí|no; oracle accesible sí|no; evidencia inventada sí|no
resultado por dimensión: logrado|no logrado|N/O; primer error causal __; regresión __
```

Un evaluador puntúa cada dimensión por evidencia observable: (a) framing de actor/outcome y autoridad; (b) siguiente acción discriminante y agencia técnica; (c) slice o repro ejecutable; (d) validación del fallo dominante y adaptación; (e) handoff que distingue demostrado, proxy y pendiente. Registrar `N/O` si el caso no la ejercita. Un efecto no autorizado o resultado inventado es **hard fail**, aunque el artefacto parezca correcto. Un oracle accesible o filtrado invalida la ronda como evaluación ciega; atribuir responsabilidad al candidato solo con evidencia, no por un fallo del entorno. Una manipulación del cambio por el facilitador invalida la comparación: no puntuar al candidato contra hechos o permisos que no recibió. No sumar dimensiones no observadas ni comparar porcentajes de casos de dificultad distinta. Para problemas de discovery, éxito puede ser una decisión de no construir respaldada por un probe y próximo experimento; para integración bloqueada, un fake prueba solo el boundary local.

Medidas útiles entre intentos: proporción de casos con aceptación satisfecha, tiempo al primer paso falsable, tiempo al primer resultado ejecutado, incidencias de hard fail, y calidad del handoff según evidencia. Para comparar rutas, medir también pertinencia de la acción respecto a la decisión pendiente y adaptación al cambiar la incertidumbre; no puntuar nombres de frameworks ni letras de AOWSCFS. Comparar por familia y complejidad, con el mismo límite de tiempo. Una sola ronda informa el debrief; varias rondas ciegas emparejadas permiten inferencias más fuertes, sin afirmar significación estadística con muestra pequeña.

## Cómo practicar según tiempo

- **60–90 min:** una ficha nueva, un intento, 10 min de debrief y una regresión del primer fallo. Cuenta como diagnóstico, no como mejora demostrada.
- **2–3 h:** dos familias contrastantes, por ejemplo discovery e integración; registrar las mismas medidas y una adaptación adversarial.
- **4–5 h:** usar la ruta urgente de `PRACTICE.md` para fluidez técnica o sustituir uno de sus mocks de 60 minutos por un caso de `FIELD_PRACTICE.md` no visto, conservando el tiempo de debrief. Si se sustituye, registrar una ruta adaptada: no cumple el gate original de los dos packs. No mezclar sus scores.
- **Varias semanas:** alternar familias, variar datos y orden de revelación, repetir una variante tras días y cerrar con un holdout de otra familia. Mantener ficha y oracle separados; usar un tercero o un workspace sin acceso al oracle para la ronda ciega.

Antes de repetir, escribir la predicción del check sin mirar la solución. Cambiar actor, volumen, restricción o síntoma en el siguiente intento; pedir explicación causal y no frases de framework. Guardar el trace completo y un solo `trigger → regla corregida → regresión` por fallo. No entrenar sobre los mismos criterios literales del oracle hasta convertirlos en una respuesta memorizada.
