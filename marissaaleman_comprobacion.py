nombre = input("Ingrese el nombre del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

asignatura = [] 
notas = []
for i in range(4):
    materia = input("Ingrese el nombre de la materia " )
    nota = float(input("Ingrese la nota de {}"))
    notas.append(nota)
    asignatura.append(materia)

total = 0
for _, nota in notas:
    total += nota
promedio = total / len(notas)

resultado = "Aprobado" if promedio >= 3.0 else "Reprobado"

print("\nResumen:")
print("Nombre del estudiante:", nombre)
print("Grado:", grado)
print("Promedio de notas:", promedio)
print("Resultado:", resultado)