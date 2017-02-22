int LED_PIN = 13;
String value;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    value = Serial.readString();
    Serial.println(value);
    if(value == "o"){
      Serial.println("You write o");
      digitalWrite(LED_PIN, HIGH);
    }
    else if (value == "f"){
      Serial.println("You write f");
      digitalWrite(LED_PIN, LOW);
    }
  }

}
