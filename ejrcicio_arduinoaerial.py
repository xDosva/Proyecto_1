import serial
 
lectura = serial.Serial('COM7', 9600)
 
# Funciones
def encender_led():
    lectura.write(b'1')
 
def apagar_led():
    lectura.write(b'2')
 
def encender_led2():
    lectura.write(b'3')
 
def apagar_led2():
    lectura.write(b'4')
 
def encender_led3():
    lectura.write(b'5')
 
def apagar_led3():
    lectura.write(b'6')
 
def encender_led4():
    lectura.write(b'7')
 
def apagar_led4():
    lectura.write(b'8')
 
# Inicio de ciclo While
while True:
    comando = input("Escribe 'encender' para encender el LED o 'apagar' para apagarlo: ").strip().lower()
   
    if comando == 'encender':
        encender_led()
        print("LED encendido")
    elif comando == 'apagar':
        apagar_led()
        print("LED apagado")
    elif comando == 'encender2':
        encender_led2()
        print("LED 2 encendido")
    elif comando == 'apagar2':
        apagar_led2()
        print("LED 3 apagado")
    elif comando == 'encender3':
        encender_led3()
        print("LED 3 encendido")
    elif comando == 'apagar3':
        apagar_led3()
        print("LED 4 apagado")
    elif comando == 'encender4':
        encender_led4()
        print("LED 4 encendido")
    elif comando == 'apagar4':
        apagar_led4()
        print("LED 4 apagado")        
 
    else:
        print("Comando no reconocido. Por favor escribe 'encender' o 'apagar'.")
