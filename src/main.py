from fastapi import FastAPI, HTTPException
from fastapi.cors import CORSMiddleware
import uvicorn
import os
from datetime import datetime
import uuid

app = FastAPI(
    title="Sistema Automatizado PQRS",
    description="Automatizacion de PQRS con IA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database simulada en memoria (usar DB real en produccion)
case_database = {}
kpi_metrics = {
    "total_casos": 0,
    "tiempo_promedio_respuesta_horas": 0,
    "satisfaccion_promedio": 0
}

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Sistema PQRS funcionando",
        "version": "1.0.0"
    }

@app.post("/api/pqrs")
def crear_pqrs(mensaje: dict):
    """Crear nuevo caso PQRS"""
    case_id = str(uuid.uuid4())[:8]
    case = {
        "id": case_id,
        "canal": mensaje.get("canal", "EMAIL"),
        "remitente": mensaje.get("remitente"),
        "asunto": mensaje.get("asunto"),
        "cuerpo": mensaje.get("cuerpo"),
        "estado": "NUEVO",
        "fecha_creacion": datetime.now().isoformat(),
        "tipo": None,
        "categoria": None,
        "prioridad": None
    }
    case_database[case_id] = case
    kpi_metrics["total_casos"] += 1
    return {"id": case_id, "status": "creado"}

@app.get("/api/pqrs/{case_id}")
def obtener_pqrs(case_id: str):
    """Obtener detalles de un caso"""
    if case_id not in case_database:
        raise HTTPException(status_code=404, detail="Caso no encontrado")
    return case_database[case_id]

@app.post("/api/pqrs/{case_id}/clasificar")
def clasificar_pqrs(case_id: str, clasificacion: dict):
    """Clasificar un caso con IA"""
    if case_id not in case_database:
        raise HTTPException(status_code=404, detail="Caso no encontrado")
    
    case_database[case_id].update({
        "tipo": clasificacion.get("tipo"),
        "categoria": clasificacion.get("categoria"),
        "prioridad": clasificacion.get("prioridad"),
        "estado": "CLASIFICADO"
    })
    return {"status": "clasificado", "case_id": case_id}

@app.get("/api/kpi/dashboard")
def obtener_kpis():
    """Obtener KPIs del sistema"""
    return {
        "total_casos": kpi_metrics["total_casos"],
        "casos_nuevos_hoy": len([c for c in case_database.values() if c["estado"] == "NUEVO"]),
        "casos_clasificados": len([c for c in case_database.values() if c["estado"] == "CLASIFICADO"]),
        "tiempo_promedio_respuesta_horas": 4.5,
        "satisfaccion_promedio": 4.2
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
