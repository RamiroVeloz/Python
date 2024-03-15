import random

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")

word_displayed = ""
#Seleccionar dificultad para el juego
diff = int(input('Ingrese un numero para seleccionar la dificultad: \n 1- Facil \n 2- Medio \n 3- Dificil \n Elija :D :'))
if (diff == 1):
    vocales = ['a', 'e', 'i', 'o', 'u']
    for x in secret_word:
        if (x in vocales):
            word_displayed += x
        else:
            word_displayed += '_'
elif (diff == 2):
    word_displayed += secret_word[0]
    word_displayed += "_" * (len(secret_word) -2)
    word_displayed += secret_word[len(secret_word)-1]
elif (diff == 3):
    word_displayed = "_" * len(secret_word)



# Mostrarla palabra parcialmente adivinada
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Palabra: {word_displayed}")

while (max_attempts > 0):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    #En caso de que el usuario ponga mas de un caracter, se tomara en cuenta solo el primero de ellos
    letter = letter[0]

    #Si se incerta un valor vacio como letra, el juego da un mensaje de error
    if letter == "" or letter == " ":
        print("Error, no se registro ninguna letra")
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        max_attempts -= 1
        continue

    # Agregar la letra a la lista de letras adivinadas 
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        max_attempts -= 1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
        word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

        # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")