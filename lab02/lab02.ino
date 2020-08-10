int pin = 2;                 // 定義 LED 燈腳位
const int t_interval = 1000; // 單位間隔時間為 1000 毫秒
void setup()
{
    Serial.begin(115200);
    pinMode(pin, OUTPUT); // 設定 pin 腳位為輸出腳位
}
void dot() // 傳送"點"
{
    digitalWrite(pin, HIGH); // 亮起 LED 燈
    delay(t_interval);
    digitalWrite(pin, LOW);
    delay(t_interval);
}
void dash() // 傳送"劃"
{
    digitalWrite(pin, HIGH);
    delay(t_interval * 3);
    digitalWrite(pin, LOW);
    delay(t_interval);
}
void loop()
{
    Serial.println("F");
    dot();
    dot();
    dash();
    dot();                 // 利用 2 種函式進行不同閃爍來表示 F
    delay(t_interval * 3); // 每個字母間隔 3000 毫秒
    Serial.println("L");
    dot();
    dash();
    dot();
    dot(); // L
    delay(t_interval * 3);
    Serial.println("A");
    dot();
    dash(); // A
    delay(t_interval * 3);
    Serial.println("G");
    dash();
    dash();
    dot(); // G
    delay(t_interval * 7);
}