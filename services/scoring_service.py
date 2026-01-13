import random
import time
from services.db_service import Session
from model import TablasAmortizacion
from typing import Literal

def audit_scoring_service(id_simulacion: int):
    # Esperamos entre 1 y 3 segundos
    time.sleep(random.uniform(1, 3))
    
    # codificamos una posibilidad del 10%
    if random.random() < 0.60:
        _update_scoring_status("FALLIDO", id_simulacion)
        raise Exception("Error en el servicio de scoring")
    
    print("La auditoria se completo con exito")
    _update_scoring_status("EXITO", id_simulacion)
    
def _update_scoring_status(result: Literal["EXITO", "FALLIDO"], id_simulacion: int):
    with Session() as session, session.begin():
        registro = session.get(TablasAmortizacion, id_simulacion)
        if registro:
            registro.estado_auditoria = result
        session.commit()