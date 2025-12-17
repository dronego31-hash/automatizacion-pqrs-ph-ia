# Sistema Automatizado de Gestión de PQRS y Comunicaciones con IA para Propiedad Horizontal

## Descripción general

Este proyecto diseña un sistema de automatización para la gestión de PQRS y comunicaciones entre residentes y administradores de propiedad horizontal, utilizando modelos de lenguaje e integración con herramientas ya disponibles (correo, formularios web, Microsoft 365, bots y flujos de trabajo automatizados).

El objetivo es reducir tiempos de respuesta, disminuir la carga operativa del administrador y mejorar la experiencia de los residentes mediante respuestas más rápidas, consistentes y trazables.

## Contexto

En la mayoría de copropiedades la gestión de quejas, solicitudes y comunicaciones se realiza de forma manual (correos, chats dispersos, llamadas), sin un sistema de clasificación ni medición de tiempos, lo que genera saturación del administrador, demoras y baja satisfacción en los residentes.

Este proyecto se enmarca dentro del Plan Estratégico de Innovación y Tecnología de ASURBE, utilizando este proceso como piloto de automatización y caso de uso de IA aplicado a la propiedad horizontal.

## Objetivos del proyecto

- Clasificar automáticamente los mensajes de residentes (tipo y prioridad) usando modelos de IA.
- Proponer respuestas base generadas por IA para revisión del administrador.
- Centralizar la trazabilidad de PQRS y comunicaciones en una base de datos estructurada.
- Medir tiempos de respuesta, volumen de casos y nivel de automatización alcanzado.

## Arquitectura propuesta

La solución se diseña de forma modular:

- **Ingesta de mensajes**: integración con correo/formularios o conectores (ej. Microsoft 365, bots, n8n/Power Automate).
- **Clasificación con IA**: modelo que etiqueta tipo de mensaje (queja, solicitud, felicitación, urgencia) y nivel de prioridad.
- **Generación de respuesta asistida**: uso de un modelo de lenguaje para generar una respuesta sugerida según el contexto y las políticas de la copropiedad.
- **Gestión y analítica**: almacenamiento de casos en una base de datos y tablero de seguimiento (KPIs de tiempos de respuesta, volumen y satisfacción).

Los detalles de la arquitectura funcional y técnica se documentan en `docs/arquitectura.md` y `docs/flujo_funcional.md`.

## Rol y responsabilidades

Este proyecto está diseñado y liderado por: Diego Escobar

- Definición del caso de uso y alcance del piloto junto con directiva y administradores.
- Diseño del flujo de extremo a extremo: captura, clasificación, enrutamiento y respuesta asistida.
- Selección de herramientas y arquitectura (M365, plataforma de automatización, APIs de modelos de lenguaje).
- Definición de KPIs y tablero de seguimiento para evaluar el impacto de la automatización.
- Diseño del plan de despliegue por fases y estrategia de cambio con administradores "early adopters".

## Datos de ejemplo

En la carpeta `data/` se incluyen:

- `ejemplos_mensajes.csv`: mensajes de ejemplo anonimizados para ilustrar el proceso de clasificación.
- `diccionario_categorias.md`: descripción de las categorías y prioridades utilizadas por el sistema.

Estos datos son sintéticos y se usan únicamente con fines demostrativos.

## Estado del proyecto

- **Fase actual**: diseño funcional y prototipo conceptual.
- **Próximos pasos**:
  - Construir un prototipo de clasificación en `notebooks/exploracion_clasificacion.ipynb`.
  - Implementar un flujo de automatización mínimo viable (MVP) con un conector de correo o formulario.
  - Definir y probar los tableros de KPIs con datos de prueba.

## Cómo contribuir / extender

Este proyecto está pensado como base para:

- Adaptar la clasificación a otros tipos de procesos administrativos.
- Integrar nuevas fuentes de datos (por ejemplo, WhatsApp Business, apps de administración de PH).
- Explorar diferentes modelos de IA para clasificación y generación de respuestas.

Cualquier sugerencia o mejora de arquitectura, flujo o métricas es bienvenida.


## Documentacion del Proyecto

El repositorio incluye documentacion completa:

### Arquitectura
- **docs/arquitectura.md**: Componentes, flujo de datos, tecnologias
- **docs/flujo_funcional.md**: Flujo end-to-end, 9 etapas del sistema

### Datos y Config
- **data/diccionario_categorias.json**: Categorias, tipos, prioridades, reglas
- **data/ejemplos_mensajes.csv**: 10 casos reales para testing
- **config/settings.json**: SLAs, KPIs, integraciones
- **.env.example**: Variables de ambiente

### Ejemplos
- **examples/prompt_clasificacion.md**: Prompts para IA
- **examples/plantillas_respuesta.md**: Plantillas por categoria
- **requirements.txt**: Dependencias Python (OpenAI, n8n, pandas, etc)
