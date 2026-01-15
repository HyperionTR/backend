from fastapi import Body, FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from schema import SimulationData, AmortizationRow
from services.math_service import calcular_tabla_francesa
from services.db_service import Session, engine
from services.scoring_service import audit_scoring_service
from model import Base, TablasAmortizacion
from typing import List

# Inicializando BD
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Forgot the CORS problem...
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def main():
    return {"message": "Hello, World!"}

@app.post('/simulate', response_model=List[AmortizationRow])
def simulate(  bg_task: BackgroundTasks, data: SimulationData = Body(...) ):
    # Calculamos los datos de la tabla de amortizacion
    tabla = calcular_tabla_francesa( data.monto, data.tasa_anual, data.plazo_meses )
    bg_task_id = 0
    
    # Guardamos datos en la BD
    with Session() as session, session.begin():
        datos_simulacion = TablasAmortizacion(
            monto = data.monto,
            tasa_anual = data.tasa_anual,
            plazo_meses = data.plazo_meses,
            tabla_resultado = tabla
        )
        session.add(datos_simulacion)
        session.flush()
        
        bg_task_id = datos_simulacion.id
    
    # Llamamos al servicio de scoring
    bg_task.add_task(audit_scoring_service, bg_task_id)
    
    return tabla


    
    
