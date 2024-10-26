def validar_letra():
    # Definir el conjunto de caracteres válidos del alfabeto español
    caracteres_validos = "abcdefghijklmnopqrstuvwxyzáéíóúñ"
    contador_invalidas = 0

    while True:
        letra = input("Ingresa una letra: ").lower()  # Convertir a minúscula inmediatamente

        if len(letra) == 1 and letra in caracteres_validos:
            return letra  # Devuelve la letra válida
        else:
            contador_invalidas += 1
            print("Por favor, ingresa solo una letra del alfabeto español.")

letra_valida = validar_letra()
print(f"La letra válida es: {letra_valida}")



def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def validar_seleccion(opcion):
    # Rechaza entradas que contengan espacios en blanco o sean vacías
    if opcion.isdigit() and opcion in ['1', '2', '3', '4']:
        return True
    return False

def ejecutar_opcion(opcion):
    if opcion == '1':
        print("Has seleccionado la Opción 1.")
    elif opcion == '2':
        print("Has seleccionado la Opción 2.")
    elif opcion == '3':
        print("Has seleccionado la Opción 3.")
    elif opcion == '4':
        print("Saliendo del programa...")
        return False
    return True

# Programa principal
def main():
    while True:
        mostrar_menu()
        seleccion = input("Por favor, selecciona una opción: ").strip()
        
        # Verifica si la entrada contiene solo espacios o es inválida
        if seleccion.isspace() or len(seleccion) == 0:
            print("Error: La entrada no puede contener solo espacios.")
        elif validar_seleccion(seleccion):
            if not ejecutar_opcion(seleccion):
                break
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")
        
if __name__ == "__main__":
    main()
#ejercicio 8
def validar_entrada(cadena):
    # Dividir la cadena por comas y eliminar espacios en blanco alrededor de las letras
    letras = [letra.strip() for letra in cadena.split(',')]
    
    # Validar que todas las entradas sean letras y no estén repetidas
    if all(letra.isalpha() for letra in letras) and len(letras) == len(set(letras)):
        return True
    return False

# Programa principal
def main():
    entrada = input("Ingresa varias letras separadas por comas: ")
    
    if validar_entrada(entrada):
        print("Entrada válida: todas las letras son únicas y válidas.")
    else:
        print("Entrada no válida: asegúrate de que todas sean letras y no estén repetidas.")

if __name__ == "__main__":
    main()
#Ejercicio 9:
def es_letra_valida(letra):
    # Validar si el input es una letra única
    return letra.isalpha() and len(letra) == 1

# Programa principal
def main():
    intentos = 0
    max_intentos = 5

    while intentos < max_intentos:
        entrada = input(f"Intento {intentos + 1}/{max_intentos}. Ingresa una letra válida: ").strip()

        if es_letra_valida(entrada):
            print(f"Entrada válida: '{entrada}' es una letra.")
            break  # Salir del bucle si se ingresó una letra válida
        else:
            print(f"'{entrada}' no es una letra válida.")
            intentos += 1

    if intentos == max_intentos:
        print("Has alcanzado el límite de intentos.")
    else:
        print("Programa finalizado exitosamente.")

if __name__ == "__main__":
    main()
#rEjercicio 10:
def es_letra_valida(letra, letras_ingresadas):
    # Verifica si es alfabética y si tiene longitud de 1
    if not letra.isalpha():
        return "Error: El carácter ingresado no es una letra."
    elif len(letra) != 1:
        return "Error: Debes ingresar solo una letra."
    elif letra in letras_ingresadas:
        return f"Error: La letra '{letra}' ya ha sido ingresada previamente."
    return True  # Es válida

# Programa principal
def main():
    intentos = 0
    max_intentos = 5
    letras_ingresadas = []

    while intentos < max_intentos:
        entrada = input(f"Intento {intentos + 1}/{max_intentos}. Ingresa una letra válida: ").strip()
        
        resultado = es_letra_valida(entrada, letras_ingresadas)
        
        if resultado is True:
            letras_ingresadas.append(entrada)
            print(f"Entrada válida: '{entrada}' es una letra.")
            break  # Salir del bucle si la entrada es válida
        else:
            print(resultado)  # Mostrar mensaje de error específico
            intentos += 1

    if intentos == max_intentos:
        print("Has alcanzado el límite de intentos.")
    else:
        print("Programa finalizado exitosamente.")

if __name__ == "__main__":
    main()
