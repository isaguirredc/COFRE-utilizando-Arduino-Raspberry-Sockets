#include <Servo.h>

Servo meuServo;

const int pinoServo = 6;
const int ledVerde = 10;     // LED verde
const int ledVermelho = 11; // LED vermelho

String senhaCorreta = "1234";
String entradaUsuario = "";

unsigned long tempoLedVerdeLigado = 0;
unsigned long tempoLedVermelhoLigado = 0;
const long tempoDesligarLed = 2000; // 2 segundos

void setup() {
  Serial.begin(9600);

  meuServo.attach(pinoServo);
  meuServo.write(0); // Começa fechado (posição original)

  pinMode(ledVerde, OUTPUT);
  pinMode(ledVermelho, OUTPUT);

  digitalWrite(ledVerde, LOW);
  digitalWrite(ledVermelho, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

    // Controle de LEDs com base no comando
    if (comando == "LIBERA_ACESSO") {
      // Senha correta - aciona LED verde
      digitalWrite(ledVerde, HIGH);   // Aciona LED verde
      digitalWrite(ledVermelho, LOW);  // Desliga LED vermelho
      tempoLedVerdeLigado = millis(); // Guarda o tempo que o LED foi ligado
      abrirCofre();
      delay(2000); // Espera 2 segundos com o portão aberto
      fecharCofre(); // Fecha o portão (volta à posição original)
    } else if (comando == "NEGA_ACESSO") {
      // Senha incorreta - aciona LED vermelho
      digitalWrite(ledVerde, LOW);    // Desliga LED verde
      digitalWrite(ledVermelho, HIGH); // Aciona LED vermelho
      tempoLedVermelhoLigado = millis(); // Guarda o tempo que o LED foi ligado
    }
  }

  // Desliga o LED verde após 2 segundos
  if (digitalRead(ledVerde) == HIGH && (millis() - tempoLedVerdeLigado >= tempoDesligarLed)) {
    digitalWrite(ledVerde, LOW);
  }

  // Desliga o LED vermelho após 2 segundos
  if (digitalRead(ledVermelho) == HIGH && (millis() - tempoLedVermelhoLigado >= tempoDesligarLed)) {
    digitalWrite(ledVermelho, LOW);
  }
}

void abrirCofre() {
  for (int angulo = 0; angulo <= 90; angulo++) {
    meuServo.write(angulo);
    delay(10);
  }
}

void fecharCofre() {
  for (int angulo = 90; angulo >= 0; angulo--) {
    meuServo.write(angulo);
    delay(10);
  }
}
