correctas = int(input("Respuestas correctas: "))
incorrectas = int(input("Respuestas incorrectas: "))
blancas = int(input("Respuestas en blanco: "))
nota = correctas * 5 - incorrectas + blancas * 0
print("Puntuación final:", nota)