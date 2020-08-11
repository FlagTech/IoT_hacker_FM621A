#include <Wire.h>
#include<Keyboard.h>

bool isRecv = false;
String str;

void setup()
{
  Wire.begin(4);                // 開啟 I2C 通訊於頻道 4
  Wire.onReceive(receiveEvent); // 執行 Wire.onReceive 設定接收資料的函式
  Serial.begin(9600);           // 開啟序列埠通訊
  Keyboard.begin();          
}

void loop()
{
  if (isRecv == true){
    recvCmd(str);  // 執行 recvCmd() 來處理收到的字串訊息
    str ="";
    isRecv = false;
  }
  delay(100);
}

void receiveEvent(int howMany)
{
  while( Wire.available())    // 當收到訊息後不斷讀取訊息內容
  {
    char c = Wire.read();     // 將收到的值轉為字元
    str += c;                 // 將各個字元加到字串變數
    Serial.print("got!");
  }
  isRecv = true;
}
//開啟記事本
void openNotepad(){ 
  Keyboard.press(KEY_LEFT_GUI);
  delay(500);
  Keyboard.press('r');
  delay(500);
  Keyboard.releaseAll();
  Keyboard.press(KEY_CAPS_LOCK);
  Keyboard.release(KEY_CAPS_LOCK);  
  delay(500);
  Keyboard.print("NOTEPAD");
  delay(500);
  Keyboard.press(KEY_CAPS_LOCK);
  Keyboard.release(KEY_CAPS_LOCK);  
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);  
}
//開啟命令提示字元
void openComd(){  
  Keyboard.press(KEY_LEFT_GUI);
  delay(500);
  Keyboard.press('r');
  delay(500);
  Keyboard.releaseAll();
  Keyboard.press(KEY_CAPS_LOCK);
  Keyboard.release(KEY_CAPS_LOCK);  
  delay(500);
  Keyboard.print("CMD");
  delay(500);
  Keyboard.press(KEY_CAPS_LOCK);
  Keyboard.release(KEY_CAPS_LOCK);  
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);    
}
//關閉應用程式
void exitApp(){
  Keyboard.press(KEY_LEFT_ALT);
  delay(500);
  Keyboard.press(KEY_F4);
  delay(50);
  Keyboard.releaseAll();
}
//處理收到的字串訊息
void recvCmd(String cmdStr){
  Serial.print(cmdStr);
  if (cmdStr == "*notepad"){
      openNotepad();
    }
  if (cmdStr == "*comd"){
      openComd();
    } 
  if (cmdStr == "*exit"){
      exitApp();
    }         
  if (cmdStr == "*capslock"){ // 開啟或關閉大寫鎖定
    Keyboard.press(KEY_CAPS_LOCK);  
    delay(50);
    Keyboard.release(KEY_CAPS_LOCK);  
    }         
  if (cmdStr == "*enter"){
    Keyboard.press(KEY_RETURN);
    delay(50);
    Keyboard.releaseAll();
    }     
  else{      
    Keyboard.print(cmdStr);  // 若無自定義操作則直接送出
  }
}
