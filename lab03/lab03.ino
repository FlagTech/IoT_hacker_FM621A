#include <Keyboard.h>

void setup() {
  Keyboard.begin();
  delay(2000);
  Keyboard.press(KEY_LEFT_GUI);
  delay(500);
  Keyboard.press('r');
  delay(500);
  Keyboard.releaseAll();
   Keyboard.print("NOTEPAD");                   //輸入文字 NOTEPAD
  delay(500);
  Keyboard.press(KEY_RETURN);                  //按下 Enter
  Keyboard.release(KEY_RETURN);
  delay(1500);                                                       //每個目標裝置開啟程式時間不同, 可視情況修改

  Keyboard.print("T");                                       //輸入字首 T
  Keyboard.press(KEY_CAPS_LOCK);          //按下 Caps Lock 鍵
  Keyboard.release(KEY_CAPS_LOCK);      //放開 Caps Lock 鍵
  delay(500);  
  Keyboard.print("HIS IS LAB ");                   //這邊在實際輸出文字會變成小寫
  Keyboard.press(KEY_CAPS_LOCK); 
  Keyboard.release(KEY_CAPS_LOCK); 
  delay(500);  
  Keyboard.print("THREE");          
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);
  delay(500);
  Keyboard.print("BADUSB TEST");
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);
  delay(500);
  Keyboard.print("T"); 
  Keyboard.press(KEY_CAPS_LOCK); 
  Keyboard.release(KEY_CAPS_LOCK);                                          
  Keyboard.print("HIS IS THE END OF TYPING");
  Keyboard.press(KEY_RETURN);
  Keyboard.release(KEY_RETURN);
  delay(500);
  Keyboard.print("BYE BYE");
  Keyboard.press(KEY_CAPS_LOCK);  
  Keyboard.release(KEY_CAPS_LOCK);
  Keyboard.end();                                               //結束鍵盤操作  
}

void loop() {
    
}
