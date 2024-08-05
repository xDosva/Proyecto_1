while True: #
    print("Seleccionar una opción") #Inicio del menú
    print("1. Sumar") #sumar
    print("2. Restar") #sestar
    print("3. Multiplicar") #sultiplicar
    print("4. Dividir") #sividir
    print("5. Raíz") #raíz
    print("6. Fin") #finalizar


    opcion = input("Ingresar un número de la opción") #Ingresar un número de las opciones


    if opcion == "1": #If  es para sumar
        print("Sumar")
        num1 = float(input("Ingresar el primer número: "))
        num2 = float(input("Ingresar el segundo número: "))
        resultado = num1 + num2
        print("el resultado de" )


    elif opcion == "2": # If es para restar
        print("Restar")
        num1 = float(input("Ingresar el primer número: "))
        num2 = float(input("Ingresar el segundo número: "))
        resultado = num1 - num2
        print(" el resultado de", resultado )


    elif opcion == "3": #el If es para multiplicar
        print("Multiplicar")
        num1 = float(input("Ingresar el primer número: "))
        num2 = float(input("Ingresar el segundo número: "))
        resultado = num1 * num2
        print(" el resultado de", resultado)


    elif opcion == "4": #el If es para dividir
        print("Dividir")
        num1 = float(input("Ingresar el primer número: "))
        num2 = float(input("Ingresar el segundo número: "))
        resultado = num1 / num2
        print("el resultado de", resultado)


    elif opcion =="5": #el if es para sacar la raíz
        num1 = float(input("Ingresar el primer número: "))
        num2 = float(input("Ingresar el segundo número: "))
        resultado = pow(num1,1/num2)
        print("el resultado de", resultado )


    elif opcion =="6": #If es para terminar
        break
    else:
        print("Opción inválida")
        print("BASICAAAAAA")