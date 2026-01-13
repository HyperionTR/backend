from typing import List

def calcular_tabla_francesa(monto: float, tasa_anual: float, plazo_meses: int) -> List:
    # el 100 es porque la tasa anual esta en porcenajes
    tasa_mensual = ( tasa_anual / (100*12) )
    cuota_fija = monto * ( tasa_mensual / (1 -  (1+tasa_mensual) ** -plazo_meses ) )
    
    tabla = [] # Tabla de amortizacion final
    capital_pendiente = monto
    
    for mes in range(1, plazo_meses + 1):
        # Calculamos interes, capital y saldo pendiente
        interes_mes = capital_pendiente * tasa_mensual
        capital_mes = cuota_fija - interes_mes
        saldo_inicial = capital_pendiente
        capital_pendiente -= capital_mes
        
        tabla.append({
			'mes': mes,
            'saldo_inicial': round(saldo_inicial, 2),
			'interes': round(interes_mes, 2),
			'capital': round(capital_mes, 2),
			'cuota': round(cuota_fija, 2),
			'saldo_pendiente': max(0, round(capital_pendiente, 2)) # Evita que el mes final tenga un valor similar a -0.00 debido a errores de punto flotante
		})
        
    return tabla