
# 13. Declara una variable inicial y asígnale la primera letra de tu nombre.

nombre = input("Ingresa tu nombre: ")  # Pide al usuario que ingrese su nombre
inicial = nombre[0]  # Obtiene la primera letra del nombre
print("La inicial de tu nombre es:", inicial)

# 14. Pide al usuario que ingrese una letra y muéstrala en pantalla.

letra = input("Ingresa una letra: ")
print("La letra ingresada es:", letra)

# 15. Declara una variable simbolo y asígnale el carácter #.

simbolo = '#'
print("O símbolo é:", simbolo)

# 16. Comprueba si un carácter ingresado es una vocal (a, e, i, o, u).

caracter = input("Ingresa un carácter: ")

if len(caracter) == 1:
    caracter = caracter.lower()  # Convertir a minúscula para simplificar la comprobación
    if caracter in "aeiou":
        print("El carácter ingresado es una vocal.")
    else:
        print("El carácter ingresado no es una vocal.")
else:
    print("Por favor, ingresa solo un carácter.")

    