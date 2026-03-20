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

print("Categorías disponibles:")

for word in my_dict:
    print(word)
    
category = input("Seleccione una categoría: ")

# Genero la lista de palabras con random.sample y la recorro
# para jugar con cada palabra de la categoria seleccionada:

words_my_dict = random.sample(my_dict[category], len(my_dict[category]))         

for word in words_my_dict:
    guessed = [] # reinicio las letras adivinadas
    attempts = 6 # reinicio los intentos
    startGame(guessed, attempts, points, word)