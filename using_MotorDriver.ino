#define motorA  8
#define motorB  6
#define PWM_motAB  9
#define motorC  10
#define motorD  5
#define PWM_motCD  11
#define LEDPIN 13

void setup() {
  // 初期設定
  pinMode(LEDPIN, OUTPUT);
  Serial.begin(9600);
  digitalWrite(motorA, LOW);
  digitalWrite(motorB, LOW);
  digitalWrite(motorC, LOW);
  digitalWrite(motorD, LOW);
}

void loop() {
  String str;
  str = Serial.readStringUntil('z');
  //シリアル読み込み
  Serial.print(str);
  for (int i = 0; i < str.length(); i++) {
    digitalWrite(LEDPIN, HIGH);
    switch (str.charAt(i)) {
      case 'R':
        right(2000);
        break;
      case 'A':
        straight(2000);
        break;
      case 'L':
        left(2000);
        break;
      case 'B':
        back(2000);
        break;
    }
    digitalWrite(LEDPIN, LOW);
  }
}

void back(int wait) {
  digitalWrite(motorA, HIGH);
  digitalWrite(motorB, LOW);
  analogWrite(PWM_motAB, 100);
  digitalWrite(motorC, HIGH);
  digitalWrite(motorD, LOW);
  analogWrite(PWM_motCD, 100);
  delay(wait);
  digitalWrite(motorC, LOW);
  digitalWrite(motorD, LOW);
  digitalWrite(motorA, LOW);
  digitalWrite(motorB, LOW);
}

void straight(int wait) {
  digitalWrite(motorA, LOW);
  digitalWrite(motorB, HIGH);
  analogWrite(PWM_motAB, 100);
  digitalWrite(motorC, LOW);
  digitalWrite(motorD, HIGH);
  analogWrite(PWM_motCD, 100);
  delay(wait);
  digitalWrite(motorC, LOW);
  digitalWrite(motorD, LOW);
  digitalWrite(motorA, LOW);
  digitalWrite(motorB, LOW);
}

void left(int wait) {
  digitalWrite(motorA, HIGH);
  digitalWrite(motorB, LOW);
  analogWrite(PWM_motAB, 100);
  digitalWrite(motorC, LOW);
  digitalWrite(motorD, HIGH);
  analogWrite(PWM_motCD, 100);
  delay(wait);
  digitalWrite(motorC, LOW);
  digitalWrite(motorD, LOW);
  digitalWrite(motorA, LOW);
  digitalWrite(motorB, LOW);
}

void right(int wait) {
  digitalWrite(motorA, LOW);
  digitalWrite(motorB, HIGH);
  analogWrite(PWM_motAB, 100);
  digitalWrite(motorC, HIGH);
  digitalWrite(motorD, LOW);
  analogWrite(PWM_motCD, 100);
  delay(wait);
  digitalWrite(motorC, LOW);
  digitalWrite(motorD, LOW);
  digitalWrite(motorA, LOW);
  digitalWrite(motorB, LOW);
}
