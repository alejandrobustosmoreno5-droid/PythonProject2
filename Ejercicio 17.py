h = int(input("Hora de salida: "))
m = int(input("Minuto de salida: "))
s = int(input("Segundo de salida: "))
t = int(input("Duración del viaje en segundos: "))
total = (h*3600 + m*60 + s + t) % 86400
hl = total // 3600
ml = (total % 3600) // 60
sl = total % 60
print(f"Llega a las {hl:02d}:{ml:02d}:{sl:02d}")