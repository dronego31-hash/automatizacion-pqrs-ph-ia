# Arquitectura del Sistema de Automatización de PQRS y Comunicaciones con IA

Este documento describe la arquitectura funcional y técnica del sistema de automatización de PQRS y comunicaciones entre residentes y administradores de propiedad horizontal, diseñado como piloto dentro del Plan Estratégico de Innovación y Tecnología de ASURBE.  

## Visión general

El sistema se basa en una arquitectura modular que integra canales de entrada (correo, formularios, bots), un motor de clasificación con IA, un generador de respuestas asistidas y una capa de gestión y analítica para trazabilidad y seguimiento de KPIs.  

El objetivo es reducir tiempos de respuesta, disminuir carga operativa del administrador y mejorar la experiencia de los residentes mediante respuestas más rápidas, consistentes y trazables.  

## Componentes principales

1. **Capa de ingestión de mensajes**
   - Fuentes posibles:
     - Correo electrónico (buzón de PQRS de la copropiedad o de la administración).
     - Formularios web (sitio de la copropiedad, intranet o portal de residentes).
     - Bots o canales de mensajería (por ejemplo, Teams, WhatsApp Business, webchat).
   - Responsabilidades:
     - Recibir y normalizar los mensajes de entrada (remitente, canal, fecha, asunto, cuerpo del mensaje, adjuntos).
     - Enviar el mensaje normalizado al flujo de clasificación (por ejemplo, mediante un workflow en n8n o Power Automate).
   - Tecnologías sugeridas:
     - Conectores de Microsoft 365 (Outlook, Forms).
     - Plataforma de automatización (n8n, Power Automate u otra similar).
     - Webhooks/HTTP para integrar otros canales.

2. **Motor de clasificación con IA**
   - Función:
     - Analizar el texto del mensaje y asignar:
       - Tipo de mensaje (queja, petición, reclamo, solicitud de información, felicitación, urgencia, etc.).
       - Nivel de prioridad (baja, media, alta, crítica).
       - Etiquetas adicionales según las políticas de la copropiedad (por ejemplo: seguridad, aseo, parqueaderos, cartera, convivencia).
   - Enfoques posibles:
     - Uso de modelos de lenguaje (LLMs) mediante API para clasificación cero-disparo o pocas muestras.
     - Entrenamiento ligero de un modelo de clasificación supervisada usando ejemplos históricos (si existen datos).
   - Entradas y salidas:
     - Entrada: texto del mensaje normalizado y metadatos básicos.
     - Salida: tipo, prioridad, etiquetas, confianza del modelo y explicación/resumen opcional.
   - Tecnologías sugeridas:
     - API de modelos de lenguaje (según proveedor elegido).
     - Scripts o funciones en Python/JavaScript integradas al flujo de automatización.
     - Notebook de exploración (`notebooks/exploracion_clasificacion.ipynb`) para prototipado y pruebas.

3. **Módulo de generación de respuesta asistida**
   - Función:
     - Generar una respuesta base sugerida para el administrador, en lenguaje claro y alineada con las políticas y el tono de la copropiedad.
   - Lógica:
     - El modelo de lenguaje recibe:
       - El mensaje original del residente.
       - El tipo y prioridad identificados.
       - Plantillas, políticas y ejemplos de respuesta (instrucciones del sistema/prompts).
     - Devuelve:
       - Una propuesta de respuesta lista para revisión y edición por parte del administrador.
   - Consideraciones:
     - El administrador siempre tiene la última palabra (respuesta asistida, no automática en esta fase).
     - Se pueden incorporar plantillas específicas por tipo de PQRS o por política interna.
   - Tecnologías sugeridas:
     - API de modelos de lenguaje.
     - Motor de plantillas (por ejemplo, uso de variables en la plataforma de automatización o en microservicio propio).

4. **Capa de gestión, almacenamiento y trazabilidad**
   - Función:
     - Registrar cada mensaje, su clasificación, estado y las interacciones asociadas.
   - Datos mínimos por caso:
     - ID del caso.
     - Datos del remitente (anonimizables para demo).
     - Canal de entrada.
     - Texto original del mensaje.
     - Tipo, prioridad y etiquetas.
     - Fecha/hora de creación, actualización y cierre.
     - Responsable asignado.
     - Respuesta enviada (o enlace a ella).
   - Opciones de almacenamiento:
     - Base de datos relacional (por ejemplo, SQL Server, PostgreSQL, MySQL).
     - Lista o tabla en Microsoft 365 (SharePoint/Lists) para un piloto rápido.
   - Integraciones:
     - Posible enlace con herramientas de ticketing existentes o módulos internos de la administración.

5. **Capa de analítica y tableros de KPIs**
   - Objetivo:
     - Medir el desempeño del proceso y el impacto de la automatización.
   - KPIs sugeridos:
     - Tiempo promedio de respuesta.
     - Tiempo promedio de cierre de PQRS.
     - Volumen de casos por tipo y prioridad.
     - Porcentaje de mensajes clasificados automáticamente.
     - Porcentaje de respuestas generadas con asistencia de IA.
   - Herramientas sugeridas:
     - Power BI, Looker Studio u otra herramienta de BI.
     - Dashboards integrados con la base de datos o listas de M365.

## Flujo de datos (alto nivel)

1. El residente envía una PQRS o mensaje (correo, formulario, bot).
2. La capa de ingestión recibe el mensaje, lo normaliza y dispara un flujo de automatización.
3. El motor de clasificación con IA etiqueta el mensaje (tipo, prioridad, etiquetas).
4. El sistema registra el caso en la base de datos/lista con su estado inicial.
5. El módulo de respuesta asistida genera una propuesta de respuesta basándose en el contenido y la clasificación.
6. El administrador revisa la propuesta, la ajusta si es necesario y la envía al residente.
7. El sistema actualiza el estado del caso, registra la respuesta y alimenta los tableros de KPIs.

## Consideraciones de seguridad y cumplimiento

- Gestión adecuada de datos personales de residentes (cumplimiento de normativas locales de protección de datos).
- Control de acceso a la información (solo administradores y personal autorizado).
- Registro de auditoría de cambios relevantes en los casos.
- Uso responsable de modelos de IA, evitando que expongan datos sensibles en logs o prompts.

## Evoluciones futuras

- Integración con más canales (por ejemplo, apps de administración de PH, plataformas como Propiedata u otras soluciones del ecosistema).  
- Mayor automatización del ciclo completo para ciertos tipos de solicitudes de baja complejidad.  
- Entrenamiento progresivo del modelo de clasificación con datos históricos reales (cuando se cuente con ellos).  
- Incorporación de encuestas de satisfacción al cierre del caso para medir impacto percibido por los residentes.
