

# 17. Declara una variable nombre y asígnale tu nombre completo.

nombre = "Ehgar Baez"  # Reemplaza "Tu Nombre Completo Aquí" con tu nombre real
print(nombre)

# 18. Une dos cadenas "Hola" y "Mundo" para formar "Hola Mundo".

cadena1 = "Hola"
cadena2 = "Mundo"
cadena_final = cadena1 + " " + cadena2  # Concatenamos las cadenas con un espacio en medio
print(cadena_final)

# 19. Pide al usuario su nombre y muéstralo junto con un mensaje de bienvenida.

nombre = input("Ingresa tu nombre: ")
print("¡Hola, " + nombre + "! Bienvenido/a.")

# 20. Crea un programa que cuente cuántas letras tiene una cadena ingresada.

cadena = input("Ingresa una cadena de texto: ")
contador = 0

for caracter in cadena:
    if caracter.isalpha():  # Verifica si el carácter es una letra
        contador += 1

print("La cadena ingresada tiene", contador, "letras.")