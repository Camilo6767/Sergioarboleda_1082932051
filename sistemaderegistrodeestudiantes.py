# Sistema de Registro de Estudiantes
# Pide datos de 5 estudiantes con validación de edad y calificación

# Listas para almacenar datos de estudiantes
nombres = []
edades = []
calificaciones = []

# Pedir datos de 5 estudiantes
for i in range(5):
    print(f"\n--- Estudiante {i+1} ---")
    
    # Pedir nombre
    nombre = input("Nombre: ").strip()
    
    # Pedir y validar edad (bucle de validación)
    edad_valida = False
    while not edad_valida:
        try:
            edad = int(input("Edad (entre 5 y 100): "))
            if 5 <= edad <= 100:
                edad_valida = True
            else:
                print("Error: La edad debe estar entre 5 y 100. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido para la edad.")
    
    # Pedir y validar calificación (bucle de validación)
    calificacion_valida = False
    while not calificacion_valida:
        try:
            calificacion = float(input("Calificación (entre 0 y 5): "))
            if 0 <= calificacion <= 5:
                calificacion_valida = True
            else:
                print("Error: La calificación debe estar entre 0 y 5. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido para la calificación.")
    
    # Guardar datos en las listas
    nombres.append(nombre)
    edades.append(edad)
    calificaciones.append(calificacion)

# Mostrar resultados finales
print("\n" + "="*60)
print("RESULTADOS DEL REGISTRO DE ESTUDIANTES")
print("="*60)

# Encontrar estudiante con calificación más alta (condicional)
indice_max = calificaciones.index(max(calificaciones))
print(f"\n📊 Estudiante con la calificación más ALTA:")
print(f"   Nombre: {nombres[indice_max]}")
print(f"   Edad: {edades[indice_max]} años")
print(f"   Calificación: {calificaciones[indice_max]}")

# Encontrar estudiante con calificación más baja (condicional)
indice_min = calificaciones.index(min(calificaciones))
print(f"\n📊 Estudiante con la calificación más BAJA:")
print(f"   Nombre: {nombres[indice_min]}")
print(f"   Edad: {edades[indice_min]} años")
print(f"   Calificación: {calificaciones[indice_min]}")

# Calcular promedio de calificaciones (acumulador)
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / len(calificaciones)
print(f"\n📊 Calificación PROMEDIO de todos los estudiantes: {promedio:.2f}")

print("\n" + "="*60)
print("FIN DEL PROGRAMA")
print("="*60)
