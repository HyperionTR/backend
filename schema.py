from pydantic import BaseModel, Field
from typing import List

class SimulationData(BaseModel):
    # Pydantic model to accept monto, tasa_anual and plaso_meses
	monto: float = Field(..., gt=0, description="Monto total del crédito", examples=[10_000])
	tasa_anual: float = Field(..., gt=0, description="Tasa de interés anual en porcentaje", examples=[12.5])
	plazo_meses: int = Field(..., gt=0, description="Plazo en meses para el pago del crédito", examples=[12])

class AmortizationRow(BaseModel):
	mes: int = Field(..., description="Número del mes", examples=[1])
	saldo_inicial: float = Field(..., description="Saldo inicial antes del pago del mes", examples=[10000])
	interes: float = Field(..., description="Monto del interés pagado en el mes", examples=[104.17])
	capital: float = Field(..., description="Monto del capital pagado en el mes", examples=[786.16])
	cuota: float = Field(..., description="Monto total a pagar en el mes", examples=[890.33])
	saldo_pendiente: float = Field(..., description="Saldo pendiente después del pago del mes", examples=[9213])