import math

def calcular_area_circulo(radio):
    return round(math.pi * radio ** 2, 2)

def calcular_hipotenusa(cateto1, cateto2):
    return round(math.sqrt(cateto1 ** 2 + cateto2 ** 2), 2)

def calcular_potencia(base, exponente):
    return round(math.pow(base, exponente), 2)

def main():
    while True:
        print("\nMenú de Calculadora Científica:")
        print("1. Calcular área de círculo")
        print("2. Calcular hipotenusa")
        print("3. Calcular potencia")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            radio = float(input("Ingresa el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es {area}")
        elif opcion == '2':
            cateto1 = float(input("Ingresa el primer cateto: "))
            cateto2 = float(input("Ingresa el segundo cateto: "))
            hipotenusa = calcular_hipotenusa(cateto1, cateto2)
            print(f"La hipotenusa es {hipotenusa}")
        elif opcion == '3':
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            potencia = calcular_potencia(base, exponente)
            print(f"El resultado de {base} elevado a {exponente} es {potencia}")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
