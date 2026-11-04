p1 = float(input("Parcial 1: "))
p2 = float(input("Parcial 2: "))
p3 = float(input("Parcial 3: "))
examen = float(input("Examen final: "))
trabajo = float(input("Trabajo final: "))
media = (p1 + p2 + p3) / 3
nota = media * 0.55 + examen * 0.30 + trabajo * 0.15
print("Calificación final:", nota)