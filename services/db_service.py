from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import TablasAmortizacion

DB_CONNSTRING = "sqlite:///./credit_sim.db"

# El argumento check_same_thread evita que sqlite lance la excepción ProgrammingError
engine = create_engine(
	DB_CONNSTRING, connect_args={"check_same_thread": False}
)

Session = sessionmaker( autoflush=False, bind=engine)

def save_simulation_data(data, tabla):
    with Session() as session, session.begin():
        datos_simulacion = TablasAmortizacion(
            monto = data.monto,
            tasa_anual = data.tasa_anual,
            plazo_meses = data.plazo_meses,
            tabla_resultado = tabla
        )
        session.add(datos_simulacion)
        session.flush()
        
        return datos_simulacion.id