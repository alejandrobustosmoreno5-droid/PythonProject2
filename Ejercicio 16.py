d = float(input("Distancia (km): "))
v1 = float(input("Velocidad rápida (km/h): "))
v2 = float(input("Velocidad lenta (km/h): "))
if v1 > v2:
tiempo = d / (v1 - v2) * 60
print("Tiempo para alcanzarlo:", tiempo, "minutos")
else:
print("La velocidad rápida debe ser mayor")