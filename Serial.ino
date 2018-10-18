void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  String str;
  str = Serial.readStringUntil('z');
  Serial.print(str);
  for(int i = 0;i < str.length();i++){
  switch(str.charAt(i)){
    case 'R':
      digitalWrite(11,HIGH);
      delay(1000);
      break;
    case 'A':
    digitalWrite(12,HIGH);
    digitalWrite(11,HIGH);
      delay(1000);
      break;
    case 'L':
    digitalWrite(12,HIGH);
      delay(1000);
      break;
  }
  digitalWrite(11,LOW);
  digitalWrite(12,LOW);
  digitalWrite(13,LOW);  }
}
