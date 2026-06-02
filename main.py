# =========================================
# SISTEMA DE NOTAS DE ESTUDIANTES
# =========================================

estudiantes = []
opcion = 0

while opcion != 4:

    print("\n========= MENÚ =========")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Mostrar promedio general")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        nombre = input("Ingrese el nombre del estudiante: ")
        nota = float(input("Ingrese la nota: "))

        if nota >= 7:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        estudiante = {
            "nombre": nombre,
            "nota": nota,
            "estado": estado
        }

        estudiantes.append(estudiante)

        print("Estudiante registrado correctamente.")

    elif opcion == 2:

        print("\n===== LISTA DE ESTUDIANTES =====")

        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            for estudiante in estudiantes:
                print("----------------------------")
                print("Nombre:", estudiante["nombre"])
                print("Nota:", estudiante["nota"])
                print("Estado:", estudiante["estado"])

    elif opcion == 3:

        if len(estudiantes) == 0:
            print("No hay datos para calcular promedio.")
        else:
            suma = 0

            for estudiante in estudiantes:
                suma += estudiante["nota"]

            promedio = suma / len(estudiantes)

            print("Promedio general:", promedio)

    elif opcion == 4:
        print("Programa finalizado.")

    else:
        print("Opción incorrecta.")