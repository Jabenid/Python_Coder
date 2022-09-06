from datetime import datetime

tiempoActual = datetime.now()

miCumple = datetime(2023,8,14)

tiempoFalta = miCumple-tiempoActual

print(tiempoFalta.days *60*60*24 + tiempoFalta.seconds)
