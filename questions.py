import random

def startGame(guessed, attempts, points, word):
    while attempts > 0:
        # Mostrar progreso
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)

        # Verificar si ganó
        if "_" not in progress:
            print("¡Ganaste!")
            points += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        if not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            if points > 0:
                points -= 1
            print("Esa letra no está en la palabra.")

        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        points = 0
        print(f"Puntos: {points}")
##########
        
my_dict = {
    "lenguaje": ["python"],
    "tipos": ["variable", "entero", "cadena"],
    "estructura": ["bucle", "funcion","variable","lista"],
}

guessed = []
attempts = 6 
points = 0
category = ""
word = ""


print("¡Bienvenido al Ahorcado!")
print()

for key in my_dict:
    print(key)
category = input("Seleccione una categoría: ")        

# Verifico que la categoria exista en my_dict
if category in my_dict:
  word = random.choice(my_dict[category.lower()])
  startGame(guessed, attempts, points, word) # el juego solo comienza si la categoria es válida
else:
    print("La categoria ingresada no existe")