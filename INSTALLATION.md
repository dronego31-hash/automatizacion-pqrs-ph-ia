# Guia de Instalacion y Configuracion

## Requisitos Previos

- Python 3.8+
- PostgreSQL 12+ (o MySQL 5.7+)
- Git
- Cuenta en OpenAI (para API key)
- Cuenta en HuggingFace (opcional)

## Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/dronego31-hash/automatizacion-pqrs-ph-ia.git
cd automatizacion-pqrs-ph-ia
```

## Paso 2: Crear Entorno Virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

## Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Paso 4: Configurar Variables de Ambiente

```bash
cp .env.example .env
```

Edita `.env` y configura:
- DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
- OPENAI_API_KEY
- MSGRAPH_CLIENT_ID, MSGRAPH_CLIENT_SECRET
- N8N_WEBHOOK_URL

## Paso 5: Inicializar Base de Datos

```bash
python scripts/init_db.py
```

## Paso 6: Ejecutar la Aplicacion

```bash
python main.py
# O con Uvicorn:
uvicorn api:app --reload
```

La aplicacion estara disponible en http://localhost:8000

## Integracion con n8n

1. En n8n, crear nuevo workflow
2. Importar archivo `examples/workflow_n8n.json`
3. Configurar credenciales de OpenAI
4. Activar workflow

## Testing

```bash
pytest tests/
pytest tests/ --cov=src
```

## Troubleshooting

**Error: No module named 'openai'**
- Solucion: pip install openai

**Error: Cannot connect to database**
- Verificar credenciales en .env
- Asegurar que PostgreSQL esta corriendo

## Support

Para preguntas o issues, consultar la documentacion en `docs/`
