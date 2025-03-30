

# 9. Declara una variable esMayor y asígnale Verdadero si edad es mayor de 18.

edad = 20  # Puedes cambiar este valor para probar diferentes edades

if edad > 18:
    esMayor = True
else:
    esMayor = False

print(esMayor)

# 10. Crea un programa que verifique si un número ingresado es positivo o negativo.

numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

  # 11.	Declara una variable llueve y usa una condición para mostrar si debes llevar paraguas. 

respuesta = input("¿Está lloviendo? (si/no): ")

if respuesta.lower() == "si":
    print("Debes llevar paraguas.")
elif respuesta.lower() == "no":
    print("No necesitas llevar paraguas.")
else:
    print("Respuesta inválida. Por favor, responde 'si' o 'no'.")

    # 12. Escribe un programa que compare dos números y muestre Verdadero si son iguales.

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

son_iguales = numero1 == numero2

print(son_iguales)

