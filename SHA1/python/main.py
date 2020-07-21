import hashlib

if __name__=="__main__":

    try:
        while True:
            text = input("\n請輸入要使用 SHA-1 雜湊的文字: ")
            s = hashlib.sha1()
            s.update(text.encode("utf-8"))
            print("\n雜湊值為:", s.hexdigest())
    except Exception as e:
        print(e.message)
    finally:
        ser.close()


