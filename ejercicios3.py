#Ejercicio 1

def seleccionar_dificultad():
    print("Selecciona un nivel de dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (5 intentos)")
    print("3. Difícil (3 intentos)")

    while True:
        try:
            nivel = int(input("Elige una opción (1, 2 o 3): "))
            if nivel == 1:
                intentos_restantes = 10
                print("Has seleccionado el nivel Fácil.")
                break
            elif nivel == 2:
                intentos_restantes = 5
                print("Has seleccionado el nivel Medio.")
                break
            elif nivel == 3:
                intentos_restantes = 3
                print("Has seleccionado el nivel Difícil.")
                break
            else:
                print("Por favor, elige una opción válida (1, 2 o 3).")
        except ValueError:
            print("Entrada no válida. Ingresa un número (1, 2 o 3).")

    return intentos_restantes


intentos = seleccionar_dificultad()
print(f"Tienes {intentos} intentos para resolver el desafío.")

#Ejercicio 2

# Representaciones de cada etapa del ahorcado
ahorcado_dibujo = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def mostrar_ahorcado(intentos_fallidos):

    print(ahorcado_dibujo[intentos_fallidos])

intentos_fallidos = 0  # Contador de intentos fallidos


for intento in range(len(ahorcado_dibujo)):
    print(f"Intento fallido número: {intento + 1}")
    mostrar_ahorcado(intentos_fallidos)
    intentos_fallidos += 1
    input("Presiona Enter para continuar...\n")  

#ejericicio 3

import unicodedata

def normalizar_palabra(palabra):
    # Normalizar la palabra para eliminar acentos y caracteres especiales
    return ''.join(
        c for c in unicodedata.normalize('NFD', palabra)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def verificar_palabra(palabra_secreta, entrada_usuario):
    # Normalizar ambas palabras para compararlas
    palabra_normalizada = normalizar_palabra(palabra_secreta)
    entrada_normalizada = normalizar_palabra(entrada_usuario)
    return palabra_normalizada == entrada_normalizada


palabra_secreta = "Corazón"  # Palabra con acento
print("Adivina la palabra secreta.")

while True:
    entrada_usuario = input("Ingresa tu intento: ")
    if verificar_palabra(palabra_secreta, entrada_usuario):
        print("¡Correcto! Has adivinado la palabra.")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

import random

def jugar_hangman():
    palabra_secreta = "programacion"
    progreso = ["_"] * len(palabra_secreta)
    intentos_restantes = 6

    while intentos_restantes > 0 and "_" in progreso:
        print("Progreso actual:", " ".join(progreso))
        print(f"Intentos restantes: {intentos_restantes}")
        
        opcion = input("Escribe una letra o 'p' para pedir una pista: ").lower()
        
        if opcion == 'p':
            letras_reveladas = set(progreso)
            letras_posibles = [letra for letra in palabra_secreta if letra not in letras_reveladas]
            
            if letras_posibles:
                letra_pista = random.choice(letras_posibles)
                for index, letra in enumerate(palabra_secreta):
                    if letra == letra_pista:
                        progreso[index] = letra
                print(f"Pista: se ha revelado la letra '{letra_pista}'")
                intentos_restantes -= 1  # Reducir intentos por usar una pista
            else:
                print("No hay letras por revelar.")
        
        elif len(opcion) == 1 and opcion.isalpha():
            if opcion in palabra_secreta:
                for index, letra in enumerate(palabra_secreta):
                    if letra == opcion:
                        progreso[index] = letra
                print(f"¡Correcto! La letra '{opcion}' está en la palabra.")
            else:
                intentos_restantes -= 1
                print(f"Incorrecto. La letra '{opcion}' no está en la palabra.")
        else:
            print("Opción no válida. Intenta de nuevo.")

    if "_" not in progreso:
        print("¡Felicidades, has adivinado la palabra:", palabra_secreta)
    else:
        print("Te has quedado sin intentos. La palabra era:", palabra_secreta)

jugar_hangman()

#Ejercicio 5 

import random
import pickle

def guardar_estado(palabra, progreso, intentos):
    with open('estado_juego.pkl', 'wb') as f:
        pickle.dump((palabra, progreso, intentos), f)
    print("Juego guardado.")

def cargar_estado():
    try:
        with open('estado_juego.pkl', 'rb') as f:
            palabra, progreso, intentos = pickle.load(f)
        print("Juego cargado.")
        return palabra, progreso, intentos
    except FileNotFoundError:
        print("No hay estado guardado.")
        return None, None, None

def jugar_hangman():
    palabra_secreta = "programacion"
    progreso = ["_"] * len(palabra_secreta)
    intentos_restantes = 6

    while True:
        print("Progreso actual:", " ".join(progreso))
        print(f"Intentos restantes: {intentos_restantes}")
        
        opcion = input("Escribe una letra, 'p' para pedir una pista, o 's' para guardar: ").lower()

        if opcion == 's':
            guardar_estado(palabra_secreta, progreso, intentos_restantes)
            continue
            
        if opcion == 'c':
            palabra_secreta, progreso, intentos_restantes = cargar_estado()
            if palabra_secreta is not None:
                continue

        if opcion == 'p':
            letras_reveladas = set(progreso)
            letras_posibles = [letra for letra in palabra_secreta if letra not in letras_reveladas]
            
            if letras_posibles:
                letra_pista = random.choice(letras_posibles)
                for index, letra in enumerate(palabra_secreta):
                    if letra == letra_pista:
                        progreso[index] = letra
                print(f"Pista: se ha revelado la letra '{letra_pista}'")
                intentos_restantes -= 1
            else:
                print("No hay letras por revelar.")
        
        elif len(opcion) == 1 and opcion.isalpha():
            if opcion in palabra_secreta:
                for index, letra in enumerate(palabra_secreta):
                    if letra == opcion:
                        progreso[index] = letra
                print(f"¡Correcto! La letra '{opcion}' está en la palabra.")
            else:
                intentos_restantes -= 1
                print(f"Incorrecto. La letra '{opcion}' no está en la palabra.")
        else:
            print("Opción no válida. Intenta de nuevo.")

        if "_" not in progreso:
            print("¡Felicidades, has adivinado la palabra:", palabra_secreta)
            break
        elif intentos_restantes <= 0:
            print("Te has quedado sin intentos. La palabra era:", palabra_secreta)
            break

jugar_hangman()


#Ejercicio 6 

import random
import json

def guardar_estado(palabra, progreso, intentos):
    estado = {
        'palabra': palabra,
        'progreso': progreso,
        'intentos': intentos
    }
    with open('estado_juego.json', 'w') as f:
        json.dump(estado, f)
    print("Juego guardado.")

def cargar_estado():
    try:
        with open('estado_juego.json', 'r') as f:
            estado = json.load(f)
        print("Juego cargado.")
        return estado['palabra'], estado['progreso'], estado['intentos']
    except FileNotFoundError:
        print("No hay estado guardado.")
        return None, None, None

def calcular_puntuacion(palabra, intentos_restantes):
    longitud_palabra = len(palabra)
    puntuacion = (longitud_palabra * 10) + (intentos_restantes * 5)
    return puntuacion

def jugar_hangman():
    palabra_secreta = "programacion"
    progreso = ["_"] * len(palabra_secreta)
    intentos_restantes = 6

    while True:
        print("Progreso actual:", " ".join(progreso))
        print(f"Intentos restantes: {intentos_restantes}")
        
        opcion = input("Escribe una letra, 'p' para pedir una pista, o 's' para guardar: ").lower()

        if opcion == 's':
            guardar_estado(palabra_secreta, progreso, intentos_restantes)
            continue
            
        if opcion == 'c':
            palabra_secreta, progreso, intentos_restantes = cargar_estado()
            if palabra_secreta is not None:
                continue

        if opcion == 'p':
            letras_reveladas = set(progreso)
            letras_posibles = [letra for letra in palabra_secreta if letra not in letras_reveladas]
            
            if letras_posibles:
                letra_pista = random.choice(letras_posibles)
                for index, letra in enumerate(palabra_secreta):
                    if letra == letra_pista:
                        progreso[index] = letra
                print(f"Pista: se ha revelado la letra '{letra_pista}'")
                intentos_restantes -= 1
            else:
                print("No hay letras por revelar.")
        
        elif len(opcion) == 1 and opcion.isalpha():
            if opcion in palabra_secreta:
                for index, letra in enumerate(palabra_secreta):
                    if letra == opcion:
                        progreso[index] = letra
                print(f"¡Correcto! La letra '{opcion}' está en la palabra.")
            else:
                intentos_restantes -= 1
                print(f"Incorrecto. La letra '{opcion}' no está en la palabra.")
        else:
            print("Opción no válida. Intenta de nuevo.")

        if "_" not in progreso:
            puntuacion = calcular_puntuacion(palabra_secreta, intentos_restantes)
            print(f"¡Felicidades, has adivinado la palabra: {palabra_secreta}!")
            print(f"Tu puntuación es: {puntuacion}")
            break
        elif intentos_restantes <= 0:
            print(f"Te has quedado sin intentos. La palabra era: {palabra_secreta}.")
            print("Tu puntuación es: 0")
            break

jugar_hangman()


#Ejercicio 7: Agregar Funcionalidad para Jugar Nuevamente

import random

def jugar_nuevamente():
    while True:
        respuesta = input("¿Deseas jugar nuevamente? (s/n): ").lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta no válida. Por favor, ingresa 's' para sí o 'n' para no.")

def jugar():
    palabras = ["python", "java", "kotlin", "javascript"]
    palabra_secreta = random.choice(palabras)
    intentos = 6
    palabra_adivinada = ["_"] * len(palabra_secreta)
    
    while intentos > 0:
        print(" ".join(palabra_adivinada))
        letra = input("Adivina una letra: ").lower()
        
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
        
        if "_" not in palabra_adivinada:
            print("¡Felicidades, has ganado!")
            break
    else:
        print(f"Lo siento, has perdido. La palabra era {palabra_secreta}.")

def main():
    while True:
        jugar()
        if not jugar_nuevamente():
            break

if __name__ == "__main__":
    main()

#Ejercicio 8: Registrar Historial de Partidas

def registrar_historial(palabra, resultado):
    with open("historial.txt", "a") as archivo:
        archivo.write(f"Palabra: {palabra}, Resultado: {resultado}\n")

def jugar():
    palabras = ["python", "java", "kotlin", "javascript"]
    palabra_secreta = random.choice(palabras)
    intentos = 6
    palabra_adivinada = ["_"] * len(palabra_secreta)
    
    while intentos > 0:
        print(" ".join(palabra_adivinada))
        letra = input("Adivina una letra: ").lower()
        
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
        
        if "_" not in palabra_adivinada:
            print("¡Felicidades, has ganado!")
            registrar_historial(palabra_secreta, "ganado")
            break
    else:
        print(f"Lo siento, has perdido. La palabra era {palabra_secreta}.")
        registrar_historial(palabra_secreta, "perdido")

if __name__ == "__main__":
    jugar()



#Ejercicio 9
def mostrar_menu_personalizacion():
    print("Menú de Personalización del Juego")
    nombre_jugador = input("Ingrese su nombre: ")
    print("Seleccione un tema de palabras:")
    print("[1] Animales")
    print("[2] Frutas")
    print("[3] Países")
    print("[4] Deportes")
    print("[5] Tecnología")
    tema_seleccionado = input("Elija un tema (1-5): ")
    musica = input("Activar música (ON/OFF): ")
    efectos = input("Activar efectos de sonido (ON/OFF): ")

    # Aquí se guardarían las opciones elegidas
    print("Cambios guardados.")
    print(f"Nombre: {nombre_jugador}, Tema: {tema_seleccionado},Música: {musica}, Efectos: {efectos}")

# Llamar a la función para mostrar el menú
mostrar_menu_personalizacion()

#ejercicio 10
import unittest


class TestAhorcado(unittest.TestCase):


    def test_guess_letter_correct(self):
        guessed_letters = []
        result = guess_letter('a', 'banana', guessed_letters)
        self.assertTrue(result)
        self.assertIn('a', guessed_letters)


    def test_guess_letter_incorrect(self):
        guessed_letters = []
        result = guess_letter('x', 'banana', guessed_letters)
        self.assertFalse(result)
        self.assertNotIn('x', guessed_letters)


    def test_guess_letter_already_guessed(self):
        guessed_letters = ['a']
        result = guess_letter('a', 'banana', guessed_letters)
        self.assertFalse(result)
        self.assertEqual(len(guessed_letters), 1)  # No se añade 'a' de nuevo


    def test_is_word_complete_true(self):
        guessed_letters = ['b', 'a', 'n']
        result = is_word_complete('banana', guessed_letters)
        self.assertTrue(result)


    def test_is_word_complete_false(self):
        guessed_letters = ['b', 'n']
        result = is_word_complete('banana', guessed_letters)
        self.assertFalse(result)


    def test_remaining_attempts(self):
        attempts = 6
        wrong_guesses = ['x', 'y', 'z']
        result = remaining_attempts(attempts, wrong_guesses)
        self.assertEqual(result, 3)  


if __name__ == '__main__':
    unittest.main()

