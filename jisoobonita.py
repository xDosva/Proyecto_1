estudiantes = [] #lista para almacenar los datos de los estudiantes

while True:
    #solicitar al usuario que ingrese el nombre y las notas del estudiantes 
    entrada = input ("ingrese el nombre del estudiantes seguido de las notas:")
    if entrada.lower() == "fin":
        break #salir del bucle si se ingresa 

    #dividir la entrada  en nombre y notas
    nombre, *notas_str = entrada.split(",") 
    notas = [int (nota) for nota in notas_str]#convertir las notas

    #calcular el promedio de las notas
    suma_notas = sum(notas)
    promedio = suma_notas / len(notas) #promedio y longirud
    estudiantes.append((nombre, notas, promedio)) 
    #mostrar en pantalla los estudiantes con sus respectivas notas 
    i = 0
    while i<len(estudiantes):
        estudiante=estudiantes[i]
        nombre,notas,promedio=estudiante
        print(f"Estudiante:{nombre}, Notas:{','.join(map(str,notas))},Promedio:{promedio}")
        i+=1 #se incrementa para a otros estuduantes
 
                        