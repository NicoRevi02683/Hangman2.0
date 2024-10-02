#ejercicio 1

palabra_nueva = input("Introduce una nueva palabra: ") 
with open('palabras.txt', 'a') as archivo: 
    archivo.write(palabra_nueva + '\n') 
print("Palabra añadida exitosamente.")

#ejercicio 2

with open('palabras.txt', 'r') as archivo:
     palabras = [linea.strip() for linea in archivo.readlines()]

palabras_unicas = list(set(palabras))


with open('palabras_unicas.txt', 'w') as archivo_unicas:
     for palabra in palabras_unicas: 
         archivo_unicas.write(palabra + '\n')

print("Archivo 'palabras_unicas.txt' creado sin duplicados.")

#ejercicio 3

with open('palabras.txt', 'r') as archivo: 
    palabras = [linea.strip() for linea in archivo.readlines()]

palabras_ordenadas = sorted(palabras)

print("Palabras ordenadas alfabéticamente:") 
for palabra in palabras_ordenadas: 
    print(palabra)

#ejercicio 4

from collections import Counter 
with open('palabras.txt', 'r') as archivo: 
    palabras = [linea.strip() for linea in archivo.readlines()] 

texto_completo = ''.join(palabras).lower() 
frecuencia = Counter(texto_completo) 

print("Frecuencia de letras:") 
for letra, conteo in frecuencia.items(): 
    print(f"{letra}: {conteo}")

#ejercicio 5

def cargar_palabras_por_longitud(longitud): 
    with open('palabras.txt', 'r') as archivo: 
        palabras = [linea.strip() for linea in archivo.readlines()] 
    palabras_filtradas = [palabra for palabra in palabras 
if len(palabra) == longitud] 
    return palabras_filtradas 
longitud_deseada = int(input("Introduce la longitud de las palabras: ")) 
palabras_seleccionadas = cargar_palabras_por_longitud(longitud_deseada) 

print("Palabras seleccionadas:") 
for palabra in palabras_seleccionadas: print(palabra)

#ejercicio 6

_palabras_cache = None 

def cargar_palabras(): 
    global _palabras_cache 
    if _palabras_cache is None: 
        with open('palabras.txt', 'r') as archivo: 
            _palabras_cache = [linea.strip() for linea in archivo.readlines()] 
    return _palabras_cache 

# Uso de la función 
palabras = cargar_palabras()

#ejercicio 7

import csv 
with open('palabras.csv', 'r') as archivo_csv: 
    lector = csv.reader(archivo_csv) 
    palabras = [fila[0] for fila in lector] 
    
print("Palabras desde CSV:") 
for palabra in palabras: 
    print(palabra)

#ejercicio 8

resultado = 'Ganó' # o 'Perdió' 
palabra_utilizada = 'ejemplo' 

with open('historial.txt', 'a') as historial: 
    historial.write(f"Resultado: {resultado}, Palabra: {palabra_utilizada}\n") 
    
print("Resultado registrado en 'historial.txt'.")

#ejercicio 9

import requests #nose porque sale asi profe, dice que no encuntra el modulo
url = 'https://ejemplo.com/palabras.txt' 
respuesta = requests.get(url) 

if respuesta.status_code == 200: 
    palabras = respuesta.text.splitlines() 
    print("Palabras descargadas:") 
    for palabra in palabras: 
        print(palabra) 
        
else: 
    print("Error al descargar el archivo.")

#ejercicio 10

from cryptography.fernet import Fernet  #nose profe tampoco lo encuentra
# Generar y guardar una clave 
clave = Fernet.generate_key() 
with open('clave.key', 'wb') as archivo_clave:
    archivo_clave.write(clave)

# Cargar la clave 
with open('clave.key', 'rb') as archivo_clave: 
    clave = archivo_clave.read() 
    
fernet = Fernet(clave) 

# Encriptar y guardar las palabras 
with open('palabras.txt', 'rb') as archivo: 
    datos = archivo.read() 

datos_encriptados = fernet.encrypt(datos)

with open('palabras_encriptadas.txt', 'wb') as archivo_encriptado: 
    archivo_encriptado.write(datos_encriptados) 
    
print("Archivo encriptado creado como 'palabras_encriptadas.txt'.") 

# Para desencriptar 
with open('palabras_encriptadas.txt', 'rb') as archivo_encriptado: 
    datos_encriptados = archivo_encriptado.read() 
    
datos_desencriptados = fernet.decrypt(datos_encriptados) 
palabras = datos_desencriptados.decode().splitlines() 

print("Palabras desencriptadas:") 
for palabra in palabras: 
    print(palabra)