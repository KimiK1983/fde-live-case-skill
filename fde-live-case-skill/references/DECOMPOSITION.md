# Decomposition compacta para un caso FDE

## Contenido

[Rutas](#rutas-de-resolución) · [Requisito operativo](#del-requisito-operativo-al-slice) · [Barrido](#barrera-de-barrido-inicial) · [Divergencia](#prueba-de-divergencia) · [Estados](#estados-y-progreso) · [Resumen](#resumen-de-cinco-frases) · [Preguntas](#preguntas-de-máximo-valor) · [Slice](#selección-del-slice) · [Contrato](#contrato-y-evidencia) · [Reorientación](#reorientación) · [Cobertura AOWSCFS](#marco-aowscfs) · [Fuentes](#fundamento-y-límites)

## Objetivo

Elegir la siguiente decisión material, obtener evidencia y actuar dentro del alcance permitido. En entrega estándar, tener baseline, contrato y slice durante el primer 20% es una referencia, no un gate. Un bug claro llega antes al repro; discovery puede usar más tiempo mientras obtenga evidencia útil.

## Rutas de resolución

Elegir por la incertidumbre que bloquea el avance, no por el nombre del framework. Las rutas son alternativas y pueden cambiar dentro del mismo caso.

| Situación | Siguiente trabajo | Evidencia suficiente para avanzar |
|---|---|---|
| **Discovery:** problema, prioridad o resultado disputados | Definir la decisión y su owner; descomponer explicaciones o palancas; priorizar por impacto abordable e incertidumbre; elegir y ejecutar el análisis o probe que podría cambiar la decisión. | Observación que apoye, refute o reabra una alternativa; recomendación condicionada y siguiente experimento con owner. No construir puede ser correcto. |
| **Entrega:** capacidad y aceptación suficientemente acordadas | Describir el requisito operativo; derivar componentes y dependencias; construir el menor recorrido verificable; comprobarlo con el usuario o dejar pendiente esa validación. | Ruta ejecutada, fallo prioritario y límite exacto de lo demostrado; siguiente paso hacia uso real con responsable y señal de outcome. |
| **Debugging/incidente:** comportamiento esperado frente a observado | Recoger repro o trazas; formular hipótesis y predicciones; ejecutar la prueba que discrimine; corregir la causa respaldada y verificar regresión. | Comparación antes/después y prueba del comportamiento afectado; incertidumbre restante explícita. Si hay impacto activo, mitigar dentro de permisos y comprobar recuperación sin esperar una explicación completa. |

En discovery, una priorización no prueba causalidad ni ahorro: distinguir volumen/tiempo expuesto de mejora atribuible. Si faltan datos, elegir una observación autorizada, un walkthrough del proceso o un experimento acotado; no inventar el resultado. Un análisis plausible sin evidencia no cierra la ruta.

Para una cifra derivada que cambie prioridad, alcance o handoff: conservar filas, periodo y unidades; mostrar cada operación y subtotal. Con herramienta local disponible, ejecutar el cálculo y cotejar su salida con el total redactado; sin ella, recomputar por otra agrupación. Comprobar que numerador y denominador describen la misma población. Si los resultados discrepan o no se puede verificar, no apoyar la recomendación en un total preciso: señalar la incertidumbre y usar solo comparaciones que sigan siendo válidas. Tiempo expuesto, cobertura y correlación no demuestran ahorro ni causalidad.

En un incidente, separar mitigación, causa respaldada y prevención. Si aparece un patrón entre clientes, registrar evidencia reutilizable y owner de plataforma sin declarar generalidad por una coincidencia.

## Del requisito operativo al slice

Cuando haya que entregar una capacidad, expresar:

`Usuario → interfaz/canal → decisión → información necesaria → acción`

Ejemplo hipotético: un operador revisa una incidencia, decide resolverla o escalarla con información autorizada y conserva el contexto del handoff. Esto describe la capacidad; no concede permiso para escribir.

Derivar solo lo necesario: entidades y fuentes para la información; reglas o inferencia para la decisión; estados, precondiciones, permisos y tools para la acción; interfaz para el usuario. Vincular el requisito al check y a la señal de outcome. No impone Foundry, una ontología, UI nueva ni un LLM.

Elegir una ruta que cruce esas piezas, no una capa horizontal aislada. Antes de uso real, identificar dependencia pendiente, quién opera/recupera y cómo observar adopción o resultado. El timebox puede limitarse a demostrar el slice y entregar ese handoff, no a implementar producción completa.

## Barrera de barrido inicial

Revisar silenciosa y proporcionalmente el contexto disponible y las omisiones materiales; AOWSCFS es una comprobación de cobertura, no un gate de exhaustividad. Terminar al tener un siguiente paso falsable y responsables para las decisiones pendientes. Con esperado y efecto claros, inspeccionar y reproducir ya satisface el barrido.

## Prueba de divergencia

Resolver por inspección los hechos recuperables. Para cada incógnita restante, comparar dos respuestas plausibles. Es material si cambian outcome, aceptación, fuente autoritativa, efecto permitido, riesgo dominante, slice o comprobación.

Después decidir por riesgo, reversibilidad y resolver disponible:

- **Inspeccionar** hechos recuperables de repo, logs, schemas, documentación o entorno.
- **Preguntar** intención, preferencia, aceptación, autoridad o efecto sensible que solo un stakeholder o política puede fijar.
- **Probar** causalidad o una hipótesis técnica con un probe seguro y reversible.
- **Reconciliar** el estado de un efecto externo incierto.
- **Decidir y registrar** una elección técnica reversible dentro del envelope confirmado.

Una decisión técnica pertenece al candidato solo si puede revertirse localmente sin cambiar aceptación, seguridad, datos protegidos, un contrato externo ni el efecto permitido. La facilidad de deshacer código no convierte una escritura externa o una decisión de producto en reversible.

## Estados y progreso

No usar un enum exclusivo que mezcle conocimiento, autoridad y progreso. Para cada incógnita material basta una línea:

```text
U1 — <confirmed | hypothesis | unknown; evidencia/procedencia> | responsable/autorización: <policy | stakeholder | candidate; alcance> | siguiente: <inspect | ask | probe | reconcile | decide> | bloquea: <none | branch | whole>; checkpoint: <...>
```

Una señal confirmada no confirma su explicación causal. Si la evidencia es correlacional, registrar por separado señal, hipótesis y predicción, alternativa material y probe/resultado. Hasta que un repro, intervención o trace discrimine las alternativas dentro del alcance, no afirmar «causa raíz» ni construir una solución dependiente de ella; sí ejecutar un probe o mitigación reversible etiquetada. El resultado puede respaldar, refutar o reabrir la hipótesis y nunca amplía autoridad.

Reglas operativas:

1. Inspeccionar antes de preguntar.
2. Decidir y registrar lo técnico reversible; una concesión nunca amplía una política o permiso superior.
   Solo una política vigente o respuesta explícita del responsable autoriza la decisión y alcance nombrados; silencio, urgencia o un `go`/`decide tú` genérico no amplían intención, aceptación ni efecto permitido.
3. Formular juntas hasta tres preguntas de mayor riesgo solo si una respuesta externa cambia la entrega. Un segundo lote es una heurística para mocks comparables, no una obligación.
4. Ante una respuesta incompleta o contradictoria, proponer una vez un aislamiento o probe seguro; después bloquear solo la rama dependiente.
5. Mientras se espera, avanzar en baseline, repro, validación de entrada, diagnóstico read-only u otro trabajo independiente aplicable.
6. Un fake solo demuestra la semántica confirmada del boundary. Si la aceptación exige integración real, no la satisface.
7. Entrar en `BLOCKED` total únicamente si no queda evidencia independiente ni harness reversible que pueda construirse sin fijar la decisión pendiente.

Handoff mínimo:

```text
BLOCKED
Pregunta al owner: "<pregunta literal>"
Rama bloqueada: <decisión y efecto>
Evidencia independiente: <comando/resultado o por qué no existe>
Mientras espero: <trabajo preservado>; próximo checkpoint: <momento>
```

Añadir opciones A/B solo cuando ayuden realmente al owner a decidir.

### Transporte de cambio del mock

`CAMBIO_AUTORIZADO` es un mecanismo de integridad del mock, no autenticación general. Cada variante de `PRACTICE.md` o `FIELD_PRACTICE.md` almacena un bloque canónico. `confirma` aporta una respuesta o evidencia dentro del alcance indicado, incluidas restricciones y datos corregidos; `delega` concede una decisión acotada sin superar permisos o políticas vigentes:

```text
CAMBIO_AUTORIZADO
caso: <identificador>
checkpoint: <momento>
tipo: <confirma | delega>
incógnita: <decisión material>
alcance: <rama o conjunto acotado>
decisión: <respuesta o autoridad concedida>
```

En el mock, el facilitador/evaluador compara marcador, orden, claves y valores contra el bloque privado; normaliza solo CRLF/LF y espacio exterior. El candidato comprueba estructura, procedencia y que caso, checkpoint y alcance correspondan a la ronda, sin acceder al oracle. La igualdad textual demuestra coincidencia con el fixture, no identidad, frescura ni autoridad fuera del mock.

En un caso en vivo, registrar una delegación verbal reportada con frase, fuente, checkpoint y alcance. Antes de una demo o efecto dependiente, pedir al candidato que confirme ese alcance con el entrevistador; una contradicción congela solo la rama afectada.

## Resumen de cinco frases

1. El actor es `<actor>`; hoy `<trabajo/problema>` y busca `<outcome o proxy>`.
2. La decisión pendiente es `<decisión>`; sigo `<discovery | entrega | debugging>` porque `<evidencia>`.
3. El usuario necesita `<información>` para `<acción>` desde `<interfaz/canal>`; fuente y efecto permitido: `<...>`.
4. Decido `<elección técnica reversible>`; `<owner>` conserva `<decisión externa>`.
5. Ejecutaré `<probe | slice | repro/fix>` y comprobaré `<resultado>`; queda `<validación/operación pendiente y owner>`.

Es una ayuda verbal, no cinco campos obligatorios ante un bug acotado.

## Preguntas de máximo valor

Elegir según divergencia y resolver, no por completar una lista:

- ¿Qué comportamiento observable define que el caso está resuelto?
- ¿Cuál requisito es obligatorio y cuál es stretch?
- ¿La integración real forma parte de la aceptación o basta probar el boundary?
- ¿Qué efecto máximo está permitido y quién lo autoriza?
- ¿Qué fallo debemos manejar explícitamente?
- ¿Qué ocurrió en un caso reciente y qué workaround se usó?

No preguntar por nombre de archivo, puerto, helper estándar u otra representación local equivalente salvo que afecte un contrato o restricción real.

## Selección del slice

Comparar cualitativamente:

`outcome/check + reducción de riesgo + cobertura end-to-end + reversibilidad - esfuerzo - dependencia externa - blast radius`

Elegir el menor slice que:

- cruza las capas necesarias;
- puede refutar una hipótesis material o verificar un requisito;
- tiene una demo simple;
- deja fuera efectos o integraciones no autorizados;
- evita credenciales o servicios frágiles salvo que sean parte de la aceptación.

Generar dos opciones solo cuando la elección cambie materialmente outcome, riesgo o aceptación.

## Contrato y evidencia

Contrato compacto:

```text
Confirmado y procedencia: ...
Decisiones técnicas reversibles que tomo: ...
Incógnita -> owner -> siguiente / alcance bloqueado: ...
Actor/outcome observable o proxy: ...
Ruta y decisión pendiente del caso: ...
Usuario/interfaz -> decisión operativa -> información -> acción: ...
Entrada -> fuente -> salida; effect envelope: ...
Probe, slice o repro/fix / no-objetivos: ...
Verification: ...
Validation observada o siguiente experimento con owner; operación pendiente: ...
Riesgo dominante / stop: ...
```

**Verification** pregunta si el artefacto cumple el contrato. **Validation** pregunta si la señal disponible indica que ayuda al actor. Un test puede verificar código; no demuestra por sí solo impacto de negocio.

Si existen varias claims materiales, usar únicamente las filas que aporten trazabilidad:

| Claim material | Source/owner | Check técnico | Señal de outcome o siguiente experimento | Resultado |
|---|---|---|---|---|

No llenar celdas con evidencia inventada; `no observado` es un resultado honesto.

## Reorientación

Ante cambio o evidencia nueva:

```text
Nueva evidencia:
Supuesto invalidado o confirmado:
Contrato / slice / check afectado:
Decisión: mantener | adaptar | recortar | handoff
Nueva evidencia a ejecutar:
```

Si el cambio entra en el timebox, recortar otra cosa y ejecutar la comprobación afectada.

## Ejemplos de decisión

- **Bug claro**: expected/observed y efecto de lectura ya están definidos. Reproducir antes de preguntar.
- **Elección reversible**: usar `dataclass` o `dict` local no cambia contrato. Elegir la convención existente, registrarla y avanzar.
- **Preferencia externa**: CSV frente a endpoint cambia el entregable aceptado. Preguntar al owner.
- **Causalidad**: no se sabe si la latencia viene de retrieval o generación. Medir ambos tramos antes de rediseñar.
- **Write unknown**: un timeout pudo ocurrir después del commit. Mantener `unknown`, reconciliar con la misma clave y no reintentar a ciegas.

## Marco AOWSCFS

Comprobar solo omisiones que cambien la siguiente acción. Estas seis lentes no son fases ni un cuestionario; `Slice` es su síntesis:

1. **Actor/owner** — quién usa, opera, decide, aprueba y recupera; no asumir que coinciden.
2. **Outcome** — cambio observable, población, baseline y métrica u otro proxy cuando aplique.
3. **Workflow** — trigger, estados, decisiones, workarounds y handoffs; distinguir lo declarado de lo observado.
4. **Systems/Data** — interfaces, fuentes, formato/frescura, acceso, provenance y ownership.
5. **Constraints** — efecto máximo, seguridad, latencia, coste, tiempo, compliance, disponibilidad y adopción.
6. **Failure modes** — técnico, semántico, humano, organizacional y efecto incierto; priorizar el dominante.
7. **Slice** — síntesis: menor ruta vertical que puede comprobar el contrato, aportar una señal del outcome o retirar el riesgo dominante.

`AOWSCFS` conserva compatibilidad como mnemónico de cobertura. No exige nombrar sus letras ni completar un inventario antes de actuar.

## Errores frecuentes

- convertir decomposition en consultoría genérica;
- mostrar un barrido completo cuando un repro ya reduce más incertidumbre;
- preguntar por elecciones técnicas reversibles;
- inventar intención, aceptación, métricas o autoridad;
- confundir un fake con aceptación de la integración;
- confundir verification con validation;
- incluir un LLM donde una regla basta;
- usar `BLOCKED` para evitar trabajo independiente;
- afirmar evidencia no ejecutada.

## Fundamento y límites

Adaptación local para casos FDE, sin afiliación empresarial ni superioridad conductual demostrada. Consultar estas fuentes durante autoría o para verificar una atribución, no como lectura obligatoria del caso:

- **Entrega:** Palantir, [use case lifecycle](https://www.palantir.com/docs/foundry/use-case-life-cycle/overview), [requisitos funcionales](https://www.palantir.com/docs/foundry/use-case-life-cycle/distilling-functional-requirements), [diseño](https://www.palantir.com/docs/foundry/use-case-life-cycle/solution-design) y [secuenciación](https://www.palantir.com/docs/foundry/use-case-life-cycle/sequencing-development). Se adapta la conexión decisión–componentes; no se exige su plataforma.
- **Discovery:** McKinsey, [resolución estructurada de problemas](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-to-master-the-seven-step-problem-solving-process). Se adapta definición, descomposición, priorización, análisis y síntesis, sin imponer siete entregables.
- **Debugging:** Google SRE, [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/). Observación, hipótesis y pruebas; mitigación no equivale a causa resuelta.

Fuentes consultadas el 28 de septiembre de 2026. La comparación de esta adaptación con la versión anterior sigue [MEASUREMENT.md](MEASUREMENT.md); un test documental no demuestra mejores decisiones.
