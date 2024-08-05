// Declaración de pines para los LEDs
const int ledPin1 = 13; // Pin del LED 1
const int ledPin2 = 12; // Pin del LED 2

void setup() {
  // Inicializar los pines de los LEDs como salidas
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  
  // Inicializar la comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Verificar si hay datos disponibles en la entrada serial
  if (Serial.available() > 0) {
    // Leer el byte desde la entrada serial
    char comando = Serial.read();
    
    // Ejecutar la acción correspondiente basada en el comando recibido
    switch (comando) {
      case '1':
        digitalWrite(ledPin1, HIGH); // Encender LED 1
        break;
      case '0':
        digitalWrite(ledPin1, LOW);  // Apagar LED 1
        break;
      case '3':
        digitalWrite(ledPin2, HIGH); // Encender LED 2
        break;
      case '2':
        digitalWrite(ledPin2, LOW);  // Apagar LED 2
        break;
      default:
        // Si el comando no es reconocido, no hacer nada
        break;
      }
  }
} 
