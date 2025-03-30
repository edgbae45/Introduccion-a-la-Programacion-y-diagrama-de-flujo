

#Ejercicio 1
#Realizar un programa que defina un vector llamado "vector_numeros" de 10 enteros, a continuación lo inicialice con valores 
# aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.

import random

# Definir el vector de 10 enteros
vector_numeros = [0] * 10

# Inicializar el vector con valores aleatorios del 1 al 10
for i in range(10):
    vector_numeros[i] = random.randint(1, 10)

# Mostrar cada elemento del vector junto con su cuadrado y su cubo
print("Elemento | Cuadrado | Cubo")
print("--------------------------")
for elemento in vector_numeros:
    cuadrado = elemento ** 2
    cubo = elemento ** 3
    print(f"{elemento:^9} | {cuadrado:^8} | {cubo:^4}")

 #Ejercicio 2
#Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado. 
# Copia los elementos del vector en otro vector pero en orden inverso, y muéstralo por la pantalla.

# Crear un vector de 5 cadenas de caracteres
vector_original = []

# Inicializar el vector con datos leídos por el teclado
for i in range(5):
    cadena = input(f"Ingresa la cadena {i + 1}: ")
    vector_original.append(cadena)

# Copiar los elementos del vector en otro vector en orden inverso
vector_inverso = vector_original[::-1]

# Mostrar el vector inverso por pantalla
print("\nVector en orden inverso:")
for cadena in vector_inverso:
    print(cadena)

#Ejercicio 3
#Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

# Crear la matriz 5x5
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Cargar la matriz con valores ingresados por el usuario
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Ingresa el valor para matriz[{i}][{j}]: "))

# Sumar filas y mostrar resultados
for i in range(5):
    suma_fila = 0
    for j in range(5):
        suma_fila += matriz[i][j]
    print(f"Suma de la fila {i + 1} es: {suma_fila}")

# Sumar columnas y mostrar resultados
for j in range(5):
    suma_columna = 0
    for i in range(5):
        suma_columna += matriz[i][j]
    print(f"Suma de la columna {j + 1} es: {suma_columna}")
