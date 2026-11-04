m2 = int(input("Monedas de 2 euros: "))
m1 = int(input("Monedas de 1 euro: "))
c50 = int(input("Monedas de 50 céntimos: "))
c20 = int(input("Monedas de 20 céntimos: "))
c10 = int(input("Monedas de 10 céntimos: "))
cent = m2*200 + m1*100 + c50*50 + c20*20 + c10*10
euros = cent // 100
centimos = cent % 100
print("Tienes", euros, "euros y", centimos, "céntimos")