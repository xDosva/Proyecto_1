# Ingresar los datos del estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
grado_estudiante = input("Ingrese el grado del estudiante: ")
 
# Listas para almacenar las asignaturas, las notas y los promedios
asignaturas = []
notas = []
promedios = []

# Ingresar las notas de las materias
for i in range(4):
    asignatura = input(f"Ingrese el nombre de la materia {i+1}: ")
    nota = float(input(f"Ingrese la nota para {asignatura}: "))
    asignaturas.append(asignatura)
    notas.append(nota)

# Calcular el promedio de las notas
promedio_total = sum(notas) / len(notas)

# Calcular el promedio de cada materia
for nota in notas:
    promedios.append(nota / len(notas))

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

# nostrar el promedio total y el promedio de cada materia
print(f"\nPromedio total: {promedio_total:.2f}")

print("\nPromedio de cada materia:")
for i in range(len(asignaturas)):
    print(f"{asignaturas[i]}: {promedios[i]:.2f}")

# Verificar si tiene derecho a recuperación o debe recursar el año

if len(reprobadas) <= 2:
    print("\nTiene derecho a recuperación.")
elif len(reprobadas) > 2:
    print("\nDebe recursar el año.")
    # Generar carta de expulsión
    with open(f"{nombre_estudiante}_carta_expulsion.txt", "w") as carta_expulsion:
        carta_expulsion.write(f"Estimado(a) {nombre_estudiante},\n\nLamentamos informarle que, debido a su desempeño académico insatisfactorio, ha sido expulsado del establecimiento. Le deseamos éxito en sus futuros esfuerzos.\n\nAtentamente,\n[Nombre del Director]")

