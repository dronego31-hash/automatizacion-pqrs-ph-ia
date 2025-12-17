# Prompts de Clasificacion con IA

## Prompt 1: Clasificador PQRS

Eres experto en propiedad horizontal. Clasifica este mensaje:

Mensaje: [TEXTO]

Responde en JSON: {tipo, categoria, prioridad, confianza, resumen}

Tipos: peticion|queja|reclamo|solicitud_informacion|felicitacion|urgencia
Categorias: seguridad|mantenimiento|convivencia|servicios|cartera|adecuacion|sanitario|administrativo
Prioridad: baja|media|alta|critica

## Prompt 2: Generador de Respuesta

Genera respuesta profesional para:

Tipo: [TIPO]
Categoria: [CATEGORIA]
Prioridad: [PRIORIDAD]
Mensaje: [MENSAJE]

Criterios:
- Empatico pero profesional
- Incluir plazo estimado
- Maximo 200 palabras
- Tono formal pero accesible

## Prompt 3: Detector Escalacion

Analiza escalacion de: [MENSAJE]

Requiere escalacion? SI/NO
Nivel? (seguridad|gerencia|legal)
Justificacion: [RESPUESTA]
