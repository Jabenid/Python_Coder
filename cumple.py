from datetime import datetime

def calcularCumple(año, mes, dia):
        
    tiempoActual = datetime.now()

    miCumple = datetime(año, mes, dia)

    tiempoFalta = miCumple-tiempoActual
    
    resultado = tiempoFalta.days *60*60*24 + tiempoFalta.seconds
    
    return resultado

