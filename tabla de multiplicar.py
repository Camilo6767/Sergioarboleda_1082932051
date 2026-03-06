# Tablas de multiplicar del 1 al 10 usando bucles anidados

for i in range(1, 11):
    print(f"Tabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Línea en blanco para separar las tablas