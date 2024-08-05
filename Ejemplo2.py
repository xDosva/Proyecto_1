import serial   

lectura = serial.Serial('COM4', 9600)  

#Funciones 
def encender_led():
    lectura.write(b'1')

def apagar_led():
    lectura.write(b'0')

def encender_led2():
    lectura.write(b'3')

def apagar_led2():
    lectura.write(b'2')

#Inicio de ciclo While
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
        print("LED 2 apagado")
    else:
        print("Comando no reconocido. Por favor escribe 'encender' o 'apagar'.")

