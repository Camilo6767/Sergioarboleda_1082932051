def validar_cedula(cedula):
    if not cedula.isdigit():
        return False
    if not (8 <= len(cedula) <= 10):
        return False
    return True

def validar_email(email):
    if '@' not in email or '.' not in email:
        return False
    return True

def validar_calificaciones(calificaciones):
    try:
        for cal in calificaciones:
            if not (0 <= cal <= 5):
                return False
        return True
    except:
        return False

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return round(sum(calificaciones) / len(calificaciones), 2)

def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"

def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        return None
    if not validar_email(email):
        return None
    if not validar_calificaciones(calificaciones):
        return None
    promedio = calcular_promedio(calificaciones)
    desempeño = clasificar_desempeño(promedio)
    return {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio,
        "desempeño": desempeño
    }

def listar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return
    print(f"{'Cédula':<10} | {'Nombre':<15} | {'Promedio':<8} | {'Desempeño'}")
    print("-" * 50)
    for est in lista_estudiantes:
        print(f"{est['cedula']:<10} | {est['nombre']:<15} | {est['promedio']:<8} | {est['desempeño']}")

def main():
    estudiantes = []
    while True:
        print("\nSistema de Gestión de Estudiantes")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            cal_str = input("Calificaciones (separadas por coma): ")
            try:
                calificaciones = [float(x.strip()) for x in cal_str.split(',')]
            except:
                print("Calificaciones inválidas.")
                continue
            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)
            if estudiante:
                estudiantes.append(estudiante)
                print(f"Estudiante agregado exitosamente. Promedio: {estudiante['promedio']} | Desempeño: {estudiante['desempeño']}")
            else:
                print("Datos inválidos. No se pudo agregar el estudiante.")
        
        elif opcion == '2':
            listar_estudiantes(estudiantes)
        
        elif opcion == '3':
            cedula_buscar = input("Cédula a buscar: ")
            encontrado = None
            for est in estudiantes:
                if est['cedula'] == cedula_buscar:
                    encontrado = est
                    break
            if encontrado:
                print(f"{encontrado['nombre']} | Promedio: {encontrado['promedio']} | Desempeño: {encontrado['desempeño']}")
            else:
                print("Estudiante no encontrado.")
        
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
