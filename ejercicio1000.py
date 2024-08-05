# Ingresar los datos del estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ") 
grado_estudiante = input("Ingrese el grado del estudiante: ")
 
# Listas para almacenar las asignaturas, las notas y los promedios
asignaturas = []  # Lista vacía para almacenar los nombres de las asignaturas
notas = []  # Lista vacía para almacenar las notas de las asignaturas
promedios = []  # Lista vacía para almacenar los promedios de las notas

# Ingresar las notas de las materias
for i in range(4):
    asignatura = input(f"Ingrese el nombre de la materia {i+1}: ")  # Solicita el nombre de la materia al usuario
    nota = float(input(f"Ingrese la nota para {asignatura}: "))  # Solicita la nota de la materia al usuario
    asignaturas.append(asignatura)  # Agrega el nombre de la materia a la lista de asignaturas
    notas.append(nota)  # Agrega la nota de la materia a la lista de notas

# Calcular el promedio de las notas
promedio_total = sum(notas) / len(notas)  # Calcula el promedio total de las notas

# Calcular el promedio de cada materia
for nota in notas:
    promedios.append(nota / len(notas))  # Calcula el promedio de cada materia y lo agrega a la lista de promedios

# Validar las notas y determinar aprobación
aprobadas = []  # Lista vacía para almacenar las asignaturas aprobadas
reprobadas = []  # Lista vacía para almacenar las asignaturas reprobadas

for i in range(len(notas)):
    if notas[i] >= 60:  # Verifica si la nota es mayor o igual a 60
        aprobadas.append(asignaturas[i])  # Agrega la asignatura a la lista de aprobadas
    else:
        reprobadas.append(asignaturas[i])  # Agrega la asignatura a la lista de reprobadas
 
# Mostrar materias aprobadas y reprobadas
print("\nMaterias aprobadas:")
for materia in aprobadas:
    print(materia)  # Imprime las materias aprobadas
 
print("\nMaterias reprobadas:")
for materia in reprobadas:
    print(materia)  # Imprime las materias reprobadas

# Mostrar el promedio total y el promedio de cada materia
print(f"\nPromedio total: {promedio_total:.2f}")  # Imprime el promedio total con dos decimales

print("\nPromedio de cada materia:")
for i in range(len(asignaturas)):
    print(f"{asignaturas[i]}: {promedios[i]:.2f}")  # Imprime el promedio de cada materia con dos decimales

# Verificar si tiene derecho a recuperación o debe recursar el año
if len(reprobadas) <= 2:  # Verifica si hay menos de dos materias reprobadas
    print("\nTiene derecho a recuperación.")  # Imprime que tiene derecho a recuperación
elif len(reprobadas) > 2:  # Verifica si hay dos o más materias reprobadas
    print("\nDebe recursar el año.")  # Imprime que debe recursar el año