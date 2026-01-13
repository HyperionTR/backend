from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_CONNSTRING = "sqlite:///./credit_sim.db"

# El argumento check_same_thread evita que sqlite lance la excepción ProgrammingError
engine = create_engine(
	DB_CONNSTRING, connect_args={"check_same_thread": False}
)

Session = sessionmaker( autoflush=False, bind=engine)
