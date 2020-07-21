#include "KbdRptParser.h"   // 匯入鍵盤解析器模組
#include <Wire.h>
String str = "<START>";         // 設定儲存資料變數
String strKey;                          // 設定收到結果變數 
char incomingStr[32];            // 設定用來傳送用的字元陣列
USB Usb;                               // 宣告 USB 物件
HIDBoot<USB_HID_PROTOCOL_KEYBOARD>    HidKeyboard(&Usb);
KbdRptParser parser;          // 宣告鍵盤解析器

void setup()
{
  delay(2000);                  
  str.toCharArray(incomingStr, 32);     // 將字串轉換成字元陣列
  Wire.begin(4);                                     // 開啟 I2C 通訊於頻道 4
  Wire.onRequest(requestEvent);       // 執行 Wire.onRequest 處理要求資料的函式
  
  Usb.Init();                                             // 初始化 USB
  delay(200);  
  HidKeyboard.SetReportParser(0, &parser);    // 設定解析器
}

void loop(){
  Usb.Task();                             // 處理 USB 任務
  strKey = parser.Getkey();     // 取得解析結果
  if (strKey.length() != 0){         // 若取得結果
     str += strKey;                       // 將取得結果放入變數
  }
}

void requestEvent() {
  str.toCharArray(incomingStr, 32);   
  Wire.write(incomingStr);            // 使用 I2C 通訊將資料傳送至 Master
  str = "";                                         // 清空變數
}
