# P1 · Latencia en una plataforma multi-cliente

**Tiempo:** 60 minutos. **Tu rol:** FDE ante un cliente que reporta lentitud de un agente de atención. No hay acceso a producción; puedes analizar estas trazas, pedir un dato discriminante y proponer un probe read-only o un repro local. No se autorizan cambios de timeout, escala o configuración real.

El cliente dice que “la IA se volvió lenta desde que subió el tráfico”. Cuatro trazas de muestra, en segundos:

| Trace | Solicitudes concurrentes | Cola/orquestador | Modelo | Tool externa | Total |
|---|---:|---:|---:|---:|---:|
| a | 2 | 0,2 | 1,3 | 0,8 | 2,3 |
| b | 3 | 0,3 | 1,4 | 0,9 | 2,6 |
| c | 20 | 3,1 | 1,5 | 0,9 | 5,5 |
| d | 24 | 4,0 | 1,4 | 1,0 | 6,4 |

Delimita qué sabes y qué solo sospechas; escoge un siguiente probe que pueda separar hipótesis. Explica cómo decidirías entre mitigación para el cliente y corrección compartida de plataforma, qué evidencia exigirías antes de declarar éxito y cómo harías handoff. Adapta tu decisión si aparece un segundo cliente afectado.
