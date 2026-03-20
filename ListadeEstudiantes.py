estudiantes = ["María", "Pedro", "Keiner","Carlos","Laura", "Luis"]

#Agregar un nuevo estudiante al final
estudiantes.append("Paula")
print(estudiantes)
estudiantes.append("Ana") 
print(estudiantes)
estudiantes.append("Jorge")
print(estudiantes)
estudiantes.append("Sofía")
print(estudiantes)

print(len(estudiantes)) #imprimir la cantidad de estudiantes

if "María" in estudiantes:
    print("María está en la lista de estudiantes.")
  
estudiantes.remove("Keiner") #Elimina la primera ocurrencia de "Keiner"
print(estudiantes)

