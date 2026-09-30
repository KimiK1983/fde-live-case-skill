# J1 · Journey por WhatsApp para tasación y cita de venta

**Tiempo:** 60 minutos. **Tu rol:** FDE con un equipo comercial. No hay canal ni sistemas reales; implementa, si aporta evidencia, una función de estado y tests locales. Ninguna reserva real ni mensaje externo está autorizado.

En este escenario sintético, una persona quiere vender su vehículo a un concesionario y envía por WhatsApp marca, modelo, año y versión (trim). Un servicio de valoración devuelve una cotización preliminar; si la persona la acepta, se ofrece una cita con un asesor para inspeccionar el vehículo. Aceptar la cotización no equivale a confirmar una reserva ni a cerrar la compraventa. Hoy el equipo mide “conversaciones contenidas sin agente”, pero algunos clientes llegan a la cita con una cotización incorrecta o desactualizada.

Propón el menor slice que preserve una cotización correcta a lo largo de la conversación y un handoff humano cuando falte certeza. Distingue salida del bot de resultado comercial; define una medida de éxito y señales de calidad. Demuestra flujo feliz y un fallo que pueda invalidar cotización o autorización. Si aparece un dato corregido durante el caso, revisa el estado y la comprobación.
