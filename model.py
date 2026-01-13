from sqlalchemy import JSON, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
	pass

class TablasAmortizacion(Base):
	__tablename__ = "tablas_amortizacion"
	
	# Datos de entrada
	id: Mapped[int] = mapped_column( primary_key=True, index=True )
	monto: Mapped[float] = mapped_column(nullable=False)
	tasa_anual: Mapped[float] = mapped_column(nullable=False)
	plazo_meses: Mapped[int] = mapped_column(nullable=False)
	
	# Datos de salida
	tabla_resultado: Mapped[dict] = mapped_column(JSON, nullable=False)
	estado_auditoria: Mapped[str] = mapped_column(default="PENDIENTE")