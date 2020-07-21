int pin = 2;  //定義 LED 燈腳位

void setup()
{
  Serial.begin(115200); 
  pinMode(pin, OUTPUT);
}

void loop()
{
  Serial.println("F");  
  dot(); dot(); dash(); dot(); //利用 2 種函式進行不同閃爍來傳送F
  delay(3000);  //每個字母間隔 3000 毫秒
  Serial.println("L");
  dot(); dash(); dot(); dot(); //L
  delay(3000);
  Serial.println("A");
  dot(); dash(); //A
  delay(3000);
  Serial.println("G");
  dash(); dash();dot(); //G
  delay(5000);
}

void dot()  //傳送"點"
{
  digitalWrite(pin, HIGH);  //亮起 LED 燈
  delay(250);
  digitalWrite(pin, LOW);
  delay(250);
}

void dash() //傳送"劃"
{
  digitalWrite(pin, HIGH);
  delay(1000);
  digitalWrite(pin, LOW);
  delay(250);
}
