# Flujo funcional del sistema de PQRS y comunicaciones con IA

Este documento describe el flujo funcional de extremo a extremo, desde que el residente envía un mensaje hasta el cierre del caso, incluyendo los puntos donde interviene la IA y la interacción del administrador.  

## 1. Recepción del mensaje

1. El residente envía una PQRS o mensaje a través de alguno de los canales habilitados:
   - Correo electrónico (buzón oficial de la copropiedad).
   - Formulario web en el sitio o portal de residentes.
   - Bot o canal de mensajería (por ejemplo, Teams, WhatsApp Business, webchat).
2. El mensaje se recibe en la bandeja o punto de entrada correspondiente.
3. Un flujo automatizado (por ejemplo, en n8n o Power Automate) se dispara cuando llega un nuevo mensaje o se envía un nuevo formulario.

Resultado: el sistema tiene un nuevo mensaje en formato bruto listo para ser procesado.  

## 2. Normalización y preparación del mensaje

1. El flujo de automatización extrae los campos relevantes:
   - Remitente (nombre, correo u otro identificador).
   - Canal de origen.
   - Fecha y hora.
   - Asunto/título del mensaje (si aplica).
   - Cuerpo del mensaje.
   - Adjuntos (si existen).
2. Se construye un objeto estandarizado (por ejemplo, en JSON) con toda la información necesaria para el siguiente paso.
3. Opcionalmente, se realiza una limpieza básica del texto (eliminar firmas, pies de página, etc.).

Resultado: se obtiene un mensaje normalizado listo para ser enviado al motor de clasificación con IA.  

## 3. Clasificación asistida por IA

1. El flujo envía el texto del mensaje (y, si se requiere, algunos metadatos) a un modelo de IA especializado en clasificación.
2. El modelo devuelve:
   - Tipo de mensaje (por ejemplo: queja, petición, reclamo, solicitud de información, felicitación, urgencia).
   - Nivel de prioridad (baja, media, alta, crítica).
   - Etiquetas temáticas (seguridad, aseo, parqueaderos, cartera, convivencia, etc.).
   - Una breve explicación o resumen opcional de por qué se asignó esa clasificación.
3. El flujo valida la respuesta del modelo:
   - Si la confianza es suficiente, se adopta la clasificación sugerida.
   - Si la confianza es baja o hay algún error, se puede marcar el caso como "requiere revisión manual de clasificación".

Resultado: el mensaje queda clasificado y priorizado de forma automática o semiautomática.  

## 4. Registro del caso y asignación

1. El sistema crea un nuevo registro de caso en la base de datos o lista seleccionada, con la siguiente información:
   - Datos del remitente (según el canal).
   - Canal de origen.
   - Texto original del mensaje.
   - Tipo, prioridad y etiquetas generadas por la IA.
   - Estado inicial (por ejemplo, "Nuevo" o "Pendiente de respuesta").
   - Fecha y hora de creación.
2. Según reglas predefinidas, el caso puede:
   - Asignarse automáticamente a un responsable (por tipo de caso o por copropiedad).
   - Quedar en una bandeja general para que el administrador lo tome manualmente.

Resultado: el caso queda registrado, visible y trazable desde el inicio.  

## 5. Generación de respuesta asistida

1. Cuando el administrador abre el caso, el sistema puede ofrecer la opción de "Generar respuesta sugerida".
2. El módulo de IA recibe:
   - El mensaje original del residente.
   - La clasificación (tipo, prioridad, etiquetas).
   - Las políticas, plantillas y lineamientos de comunicación configurados.
3. El modelo de lenguaje genera una propuesta de respuesta que:
   - Responde de forma clara y respetuosa al residente.
   - Se alinea con el tipo de mensaje y la prioridad.
   - Evita compromisos que no estén autorizados según las políticas.
4. La respuesta sugerida se presenta al administrador en un editor para que pueda:
   - Revisar el contenido.
   - Ajustar redacción, agregar detalles o anexar archivos si es necesario.
   - Aprobar la versión final para envío.

Resultado: el administrador cuenta con una respuesta base bien estructurada, reduciendo el tiempo de redacción.  

## 6. Envío de la respuesta al residente

1. Una vez revisada y aprobada, el administrador envía la respuesta desde el mismo sistema o a través del canal de origen:
   - Respuesta por correo electrónico.
   - Mensaje a través del bot o canal de mensajería.
   - Notificación en el portal de residentes.
2. El flujo de automatización registra:
   - Fecha y hora de envío.
   - Canal utilizado.
   - Versión final de la respuesta.

Resultado: el residente recibe una respuesta oportuna y el sistema mantiene un historial completo de la interacción.  

## 7. Actualización de estado y seguimiento

1. Al enviar la respuesta, el estado del caso se actualiza automáticamente (por ejemplo, de "Pendiente de respuesta" a "Respondido").
2. Si el proceso requiere una acción adicional (por ejemplo, una visita técnica o reunión), se puede mantener el caso en estado "En seguimiento" hasta su cierre definitivo.
3. Cuando se considera resuelto, el administrador cambia el estado a "Cerrado", registrando la fecha de cierre.

Resultado: cada caso tiene un ciclo de vida claro, desde su creación hasta el cierre, con todos los cambios registrados.  

## 8. Alimentación de tableros e indicadores

1. Los datos de los casos (tiempos, tipos, prioridades, estados) se sincronizan con el modelo de datos del dashboard de KPIs.
2. Las métricas principales que se pueden visualizar incluyen:
   - Tiempo promedio de primera respuesta.
   - Tiempo promedio de cierre.
   - Volumen de casos por tipo, prioridad y canal.
   - Porcentaje de casos clasificados automáticamente.
   - Porcentaje de casos con respuesta generada con apoyo de IA.
3. Estos indicadores permiten a la administración y a ASURBE:
   - Identificar cuellos de botella.
   - Priorizar mejoras de proceso.
   - Evaluar el impacto del piloto de automatización con IA.

Resultado: el sistema no solo responde y gestiona casos, sino que se convierte en una fuente de información para decisiones de mejora continua.  

## 9. Escenarios especiales

- **Mensajes urgentes o críticos**  
  - Si la clasificación detecta prioridad crítica (por ejemplo, temas de seguridad o emergencias), el flujo puede:
    - Enviar una alerta inmediata (correo, Teams, SMS) a responsables clave.
    - Requerir confirmación de lectura o atención.
- **Casos sin suficiente información**  
  - El sistema puede generar una respuesta asistida solicitando aclaraciones o datos adicionales antes de continuar el trámite.
- **Mensajes fuera del alcance**  
  - Cuando el contenido no corresponde a la administración de la copropiedad, la respuesta asistida puede incluir mensajes estándar de redirección o aclaración.

---

Este flujo funcional sirve como base para la implementación incremental: primero como prototipo conceptual y luego como MVP en una copropiedad piloto, manteniendo siempre al administrador como responsable final de la comunicación.
