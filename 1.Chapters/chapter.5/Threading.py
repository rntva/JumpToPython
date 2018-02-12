import threading
import time

# def say(msg) :
#     while 1 :
#         time.sleep(1)
#         print(msg)
#
# for msg in ["you", "need", "python"] :
#     t = threading.Thread(target=say, args=(msg,))
#     t.daemon = True
#     t.start()
#
# for i in range(100) :
#     time.sleep(0.1)
#     print(i)

class MyThread(threading.Thread) :
    def __init__(self, msg) :
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True

    def run(self) :
        while 1 :
            time.sleep(1)
            print(self.msg)

for msg in ["you", "need", "python"] :
    t = MyThread(msg)
    t.start()

for i in range(100) :
    time.sleep(0.1)
    print(i)