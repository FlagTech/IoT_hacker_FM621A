"""F-Utility FM621A LAB用工具"""
from hashlib import sha1
from ubinascii import hexlify

def permutations(iterable, r=None):    
    """permutations(range(3), 2) --> (0,1) (0,2) (1,0) (1,2) (2,0) (2,1)"""
    pool = tuple(iterable)
    n = len(pool)
    if r is None:
        r = n
    indices = list(range(n))
    cycles = list(range(n - r + 1, n + 1))[::-1]
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
        
def decrypt_sha1(sha1_value, all_letters):
    """decrypt_sha1(sha1_value, all_letters): 傳回將 sha1_value 與 all_letters 進行 4-8 位數不重複字元組合, 比對後的相同值"""
    counter = 0
    if len(sha1_value)!=40:
        print('error')
        return
    sha1_value=sha1_value.lower()
    for k in range(4,9):
        for item in permutations(all_letters,k):                       
            item=''.join(item)
            #print (item)
            #print('.',end='')
            counter += 1
            if counter >= 1000 :
                print ('=', end='')
                counter = 0
            if hexlify(sha1(item.encode()).digest()).decode("utf-8") ==sha1_value:
                return item