# MVP Roadmap - Guia de Implementacion Real

## Tiempo estimado: 5-7 dias laborales

## FASE 1: PREPARACION DEL ENTORNO (1 dia)

### 1.1 Clonar y configurar localmente
```bash
git clone https://github.com/dronego31-hash/automatizacion-pqrs-ph-ia.git
cd automatizacion-pqrs-ph-ia
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 1.2 Crear archivo .env local
```bash
cp .env.example .env
```

Editar `.env` con:
- DB_HOST=localhost
- DB_PORT=5432
- DB_NAME=pqrs_dev
- DB_USER=postgres
- DB_PASSWORD=tu_password
- OPENAI_API_KEY=sk-xxxxx

### 1.3 Instalar PostgreSQL
- Windows: https://www.postgresql.org/download/windows/
- Mac: brew install postgresql
- Linux: sudo apt-get install postgresql

Crear base de datos:
```bash
psql -U postgres
CREATE DATABASE pqrs_dev;
```

## FASE 2: ESTRUCTURA BASE DEL CODIGO (1 dia)

### 2.1 Crear estructura de carpetas
```
src/
  api/
    __init__.py
    main.py
    endpoints.py
  models/
    __init__.py
    pqrs.py
    user.py
  services/
    __init__.py
    classification.py
    response_generator.py
  database/
    __init__.py
    db.py
    models.py
  config/
    __init__.py
    settings.py
tests/
  __init__.py
  test_api.py
main.py
```

### 2.2 Crear main.py basico
```python
from fastapi import FastAPI
from fastapi.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="PQRS Automatizado")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## FASE 3: MODELOS DE DATOS (1 dia)

### 3.1 Crear modelo PQRS en src/database/models.py
```python
from sqlalchemy import Column, String, DateTime, Enum, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PQRS(Base):
    __tablename__ = "pqrs"
    
    id = Column(String, primary_key=True)
    canal = Column(String)  # EMAIL, TEAMS, etc
    remitente = Column(String)
    asunto = Column(String)
    cuerpo = Column(String)
    tipo = Column(String)  # peticion, queja, reclamo
    categoria = Column(String)
    prioridad = Column(String)  # baja, media, alta, critica
    confianza = Column(Float)
    estado = Column(String)  # NUEVO, ASIGNADO, etc
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_cierre = Column(DateTime, nullable=True)
    respuesta = Column(String, nullable=True)
```

## FASE 4: API REST CON FASTAPI (1 dia)

### 4.1 Crear endpoints en src/api/endpoints.py

**POST /api/pqrs**
- Recibe mensaje de entrada
- Lo guarda en DB
- Retorna ID del caso

**POST /api/pqrs/{id}/clasificar**
- Llama a OpenAI para clasificar
- Actualiza el caso en DB
- Retorna clasificacion

**POST /api/pqrs/{id}/generar-respuesta**
- Genera respuesta asistida
- Retorna propuesta

**GET /api/kpi/dashboard**
- Retorna metricas KPI

## FASE 5: INTEGRACION OPENAI (1 dia)

### 5.1 Crear servicio en src/services/classification.py
```python
import openai

def clasificar_pqrs(mensaje: str) -> dict:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "Clasifica este PQRS...",
            "role": "user",
            "content": mensaje
        }]
    )
    return response.choices[0].message.content
```

## FASE 6: FLUJO n8n (1 dia)

### 6.1 Configurar n8n
1. Instalar n8n: npm install -g n8n
2. Ejecutar: n8n start
3. Ir a: http://localhost:5678
4. Importar: examples/workflow_n8n.json
5. Configurar webhook hacia localhost:8000

## FASE 7: TESTING Y DEPLOYMENT (1 dia)

### 7.1 Tests basicos
```bash
pytest tests/ -v
```

### 7.2 Ejecutar MVP
```bash
python main.py
```

### 7.3 Probar endpoints
```bash
curl -X POST http://localhost:8000/api/pqrs \
  -H "Content-Type: application/json" \
  -d '{"canal":"EMAIL","remitente":"test@example.com","asunto":"Prueba","cuerpo":"Mensaje de prueba"}'
```

## Checklist de Implementacion

- [ ] PostgreSQL instalado y DB creada
- [ ] Entorno virtual Python activado
- [ ] Dependencias instaladas (requirements.txt)
- [ ] OpenAI API key configurada
- [ ] Estructura de carpetas creada
- [ ] Modelos SQLAlchemy definidos
- [ ] 4 endpoints FastAPI funcionando
- [ ] Integracion OpenAI probada
- [ ] n8n configurado y conectado
- [ ] Tests pasando
- [ ] MVP corriendo en localhost:8000

## Contacto

Para preguntas o bloqueos durante la implementacion, refer
se a:
- docs/arquitectura.md - Comprension del diseno
- docs/flujo_funcional.md - Flujo de procesos
- INSTALLATION.md - Problemas comunes
