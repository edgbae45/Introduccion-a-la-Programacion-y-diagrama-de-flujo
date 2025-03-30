

# 23.Crear una matriz de 2x2 e imprimir el promedio de todos sus elementos.

matriz = [[1, 2], [3, 4]]  # Puedes cambiar estos valores
suma = 0
contador = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        contador += 1

promedio = suma / contador
print("El promedio de los elementos de la matriz es:", promedio)

# 24.Crear una matriz 2x3 y luego transponerla (convertir filas en columnas y viceversa).

matriz = [[1, 2, 3], [4, 5, 6]]  # Matriz 2x3 original

# Transponer la matriz
matriz_transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Imprimir la matriz transpuesta
print("Matriz Transpuesta:")
for fila in matriz_transpuesta:
    print(fila)