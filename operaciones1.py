num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
operacion = int(input("1. Suma \n3. Multiplicación \nIntroduce el número de tu operación: "))

if operacion == 1:
    print(f"La suma de {num1} y {num2} da {num1 + num2}")

if operacion == 3:
    print(f"La multiplicación de {num1} y {num2} da {num1 * num2}")
