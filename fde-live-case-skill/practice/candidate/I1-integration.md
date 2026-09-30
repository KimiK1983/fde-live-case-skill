# I1 · Ticketing empresarial con resultado incierto

**Tiempo:** 60 minutos. **Tu rol:** FDE integrando una API ITSM ajena. No hay credenciales ni red al proveedor; modela el boundary con un fake local y pruebas reproducibles. No se autoriza cambiar scopes ni escribir en producción.

El flujo crea un ticket cuando un operador confirma un incidente. `POST /tickets` acepta `operation_id` y `Idempotency-Key`. En sandbox, un POST puede agotar el tiempo de espera **después** de que el servidor haya creado el ticket. `GET /operations/{operation_id}` devuelve `applied`, `not_found` o error. La documentación del cliente no garantiza que los permisos del service principal de producción coincidan con los de sandbox.

**Contrato del fake acordado para este ejercicio, no garantía de un proveedor real:**

- `operation_id` y `Idempotency-Key` identifican una misma intención dentro de un tenant y la acción de crear ticket. Permanecen estables durante toda la ronda, incluidos reinicios del cliente. El fake conserva el registro durante toda la ronda; fuera de ese horizonte no hay garantía declarada.
- Para la misma intención y payload, solicitudes repetidas o concurrentes producen como máximo un ticket y devuelven su resultado registrado. Reutilizar una clave con otro payload se rechaza sin otro efecto. El mecanismo interno es una decisión técnica del candidato.
- GET=`applied` confirma creación y devuelve el identificador del ticket. GET=`not_found` es, **en este fake**, una ausencia autoritativa: el intento anterior terminó sin efecto y no queda trabajo pendiente capaz de aplicarlo después. Un error, timeout o respuesta no interpretable no ofrece esa garantía. Los permisos reales siguen sin confirmar.

Diseña e implementa el mínimo flujo que no duplique tickets cuando el resultado es incierto. Muestra un caso feliz, un timeout tras aplicar y el fallo prioritario. Separa lo probado localmente de lo que aún requeriría validación con IT/proveedor. Si cambia una restricción durante la sesión, ajusta la estrategia y el handoff.
