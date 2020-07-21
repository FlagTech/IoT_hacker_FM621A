import network
import ESP8266WebServer     # 匯入網站模組
from machine import Pin, I2C

ssid = "LAB04_WbadUSB"
password = "12345678"
ard_i2c_addr = 4

def handleCmd(socket, args):                        # 處理 /cmd 指令的函式
    if 'bd' in args:                                # 檢查是否有 bd 參數
        i2c.writeto(ard_i2c_addr, args['bd'])
        ESP8266WebServer.ok(socket, "200", "OK")    # 回應 OK 給瀏覽器
    else:
        ESP8266WebServer.err(socket, "400", "ERR")  # 回應 ERR 給瀏覽器

print("啟動中...")
ap = network.WLAN(network.AP_IF)            # 取得基地台介面
ap.active(True)                             # 啟用基地台
ap.config(essid=ssid, password=password)    # 設定基地台 SSID 及密碼
i2c = I2C(scl=Pin(5), sda=Pin(4))           # 設定 i2c 腳位       
print("已啟動")

ESP8266WebServer.begin(80)                  # 啟用網站
ESP8266WebServer.onPath("/cmd",handleCmd)   # 指定處理指令的函式
ESP8266WebServer.setDocPath("/bd_usb")      # 指定 HTML 檔路徑

while True:
    ESP8266WebServer.handleClient()     # 持續檢查是否收到新指令





