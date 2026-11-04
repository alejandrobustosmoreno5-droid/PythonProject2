sueldo = float(input("Sueldo base: "))
v1 = float(input("Venta 1: "))
v2 = float(input("Venta 2: "))
v3 = float(input("Venta 3: "))
comision = (v1 + v2 + v3) * 0.10
total = sueldo + comision
print("Comisiones:", comision)
print("Total a cobrar:", total)