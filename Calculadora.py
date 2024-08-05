# Función q sirve para restar dos numeros
def sumar(a, b):
    return a + b

# Funcion que sirve para restar 2 numeros
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b != 0:
        return a / b

# Función principal que maneja la calculadora
def calculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

 #ciclo para dejar al usuario  quer escoja una opcion
    while True:
        opcion = input("Escoja una opción (1,2,3,4,5): ")
        
        if opcion == '5':
            print("es todo")
            break
        
        if opcion in ('1', '2', '3', '4'):
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                print("Resultado:", sumar(num1, num2))
            elif opcion == '2':
                print("Resultado:", restar(num1, num2))
            elif opcion == '3':
                print("Resultado:", multiplicar(num1, num2))
            elif opcion == '4':
                print("Resultado:", dividir(num1, num2))
        else:
            print("Opción inválida. Por favor, ingrese 1, 2, 3, 4 o 5.")

calculadora()
