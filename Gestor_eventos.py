import datetime

def crear_evento(nombre, dia, mes, año):
    fecha = datetime.date(año, mes, dia)
    return {"nombre": nombre, "fecha": fecha}

def dias_hasta_evento(fecha_evento):
    hoy = datetime.date.today()
    delta = fecha_evento - hoy
    return delta.days

def evento_pasado(fecha_evento):
    hoy = datetime.date.today()
    return fecha_evento < hoy

def main():
    nombre = input("Ingresa el nombre del evento: ")
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))
    
    evento = crear_evento(nombre, dia, mes, año)
    
    if evento_pasado(evento["fecha"]):
        dias_pasados = -dias_hasta_evento(evento["fecha"])  # Since it's negative
        print(f"El evento ya pasó. Fue hace {dias_pasados} días.")
    else:
        dias_faltan = dias_hasta_evento(evento["fecha"])
        if dias_faltan == 0:
            print("El evento es hoy.")
        else:
            print(f"Faltan {dias_faltan} días para tu evento.")

if __name__ == "__main__":
    main()
