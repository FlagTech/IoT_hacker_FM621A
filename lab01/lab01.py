from futil import decrypt_sha1
from time import time

all_letters = 'abcdefghijklmnopqrstuvwxyz'
sha1_value = '112f3a99b283a4e1788dedd8e0e5d35375c33747'#設定目標雜湊值, 這裡使用 flag 作為目標

start = time()#先使用 time 來記錄開始時間
result = decrypt_sha1(sha1_value, all_letters)#設定變數來判斷是否有結果, 傳入目標雜湊值和字庫進行暴力破解

if result:
    print('\n Success: '+sha1_value+'==>'+result)#這邊使用 "+" 號來將字串相加後顯示
else:
    print('\n Failed.')
print('Time used:', time()-start, 's')#最後將現在時間減掉開始時間並顯示出結束時間
