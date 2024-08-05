# una lista predefinida de nombres de estduiantes
guapas = ['Rose', 'Jisoo', 'Lisa']

# dejar que el usuario ingrese numbres de estudiantes
for estudiantes in range(3):
    nombre_adicional = input("Ingresar un nombre adicional: ")
    guapas.append(nombre_adicional)

# Mostrar la lista actualizada de estudiantes
print("Lista actualizada de estudiantes:", guapas)




# Ingresar los datos del estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
grado_estudiante = input("Ingrese el grado del estudiante: ")

# Listas para almacenar las asignaturas y las notas
asignaturas = []
notas = []

# Ingresar las notas de las materias
for i in range(4):
    asignatura = input(f"Ingrese el nombre de la materia {i+1}: ")
    nota = float(input(f"Ingrese la nota para {asignatura}: "))
    asignaturas.append(asignatura)
    notas.append(nota)

# Validar las notas y determinar aprobación
aprobadas = []
reprobadas = []

for i in range(len(notas)):
    if notas[i] >= 60:
        aprobadas.append(asignaturas[i])
    else:
        reprobadas.append(asignaturas[i])

# Mostrar materias aprobadas y reprobadas
print("\nMaterias aprobadas:")
for materia in aprobadas:
    print(materia)

print("\nMaterias reprobadas:")
for materia in reprobadas:
    print(materia)