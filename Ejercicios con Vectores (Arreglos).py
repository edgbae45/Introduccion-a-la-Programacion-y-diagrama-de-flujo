

# 21.Crear un vector con 5 elementos e imprimir la suma de todos los elementos del vector..

vector = [10, 20, 30, 40, 50]  # Puedes cambiar estos valores
suma = 0

for elemento in vector:
    suma += elemento

print("La suma de los elementos del vector es:", suma)

# 22.Crear un vector con 4 elementos e imprimir el resultado de multiplicar cada elemento del vector por un escalar.

vector = [1, 2, 3, 4]  # Puedes cambiar estos valores
escalar = float(input("Ingresa el valor del escalar: "))

print("Resultado de multiplicar el vector por el escalar:")

for elemento in vector:
    resultado = elemento * escalar
    print(resultado)