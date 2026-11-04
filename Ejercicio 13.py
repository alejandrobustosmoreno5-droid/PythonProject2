n = float(input("Introduce un número: "))
if n < 0:
cuadrada = "No tiene raíz cuadrada real"
cubica = -((-n) ** (1/3))
else:
cuadrada = n ** 0.5
cubica = n ** (1/3)
print("Raíz cuadrada:", cuadrada)
print("Raíz cúbica:", cubica)