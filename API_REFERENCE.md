# API Reference

## Endpoints Principales

### POST /api/pqrs/clasificar
Clasifica un mensaje automaticamente usando IA.

Request:
```json
{
  "mensaje": "texto del mensaje",
  "canal": "EMAIL",
  "remitente": "usuario@example.com"
}
```

Response (200):
```json
{
  "tipo": "peticion",
  "categoria": "mantenimiento",
  "prioridad": "media",
  "confianza": 0.87,
  "resumen": "Solicitud de reparacion"
}
```

### GET /api/pqrs/{id}
Obtiene los detalles de un caso PQRS.

Response (200):
```json
{
  "id": "MSG001",
  "tipo": "peticion",
  "estado": "EN_GESTION",
  "prioridad": "media",
  "fecha_creacion": "2025-12-17T14:30:00",
  "respuesta_generada": "Texto de respuesta..."
}
```

### POST /api/pqrs/{id}/respuesta
Genera una respuesta asistida por IA.

Request:
```json
{"incluir_propuesta": true}
```

Response (200):
```json
{
  "respuesta_propuesta": "Estimado...",
  "confianza": 0.92
}
```

### GET /api/kpi/dashboard
Obtiene metricas y KPIs del sistema.

Response (200):
```json
{
  "tiempo_promedio_respuesta_horas": 4.5,
  "tiempo_promedio_cierre_dias": 2.3,
  "volumen_casos_hoy": 12,
  "satisfaccion_promedio": 4.2
}
```

## Codigos de Error

- 400: Bad Request
- 401: No autorizado
- 404: Recurso no encontrado
- 500: Error del servidor

## Autenticacion

Todos los endpoints requieren JWT token en header:
```
Authorization: Bearer <token>
```
