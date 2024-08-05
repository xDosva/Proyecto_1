# Creamos una lista vacía para almacenar las asignaturas
asignaturas = [ ]

# Ciclo para ingresar las asignaturas
while True:
    asignatura = input("Ingrese el nombre de la asignatura (o escriba 'fin')para terminar:")

    #Verificamos si el usuario desea terminar de ingresar asignaturas
    if asignatura.lower() == 'fin':
        break
    # Agregamos la asignatura a la lista
    asignaturas.append(asignatura)

# Mostramos la lista de asignaturas por pantalla
print("Las asignaturas del curso son:")
print(",".join(asignaturas))