# try :
#     a = 4 / 0
#     b = [1,2,3]
#     print(b[3])
# except ZeroDivisionError as e : print(e)
# except IndexError as f : print(f)

class error :
    def error_raise(self):
        print("Error")

a = error()

a.error_raise()