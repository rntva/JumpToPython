#함수 리턴값 받아서 프린트
import sys

def greet_users(str_list) :
    result = ""
    for x in usernames :
        temp2 = ""
        temp = list(x)
        temp1 = str(temp[0]).upper()

        for y in temp[1:] :
            temp2 = temp2 + str(y)

        result += temp1 + temp2 + ' '
    result = result[:-1]
    return result

usernames = sys.argv[1:]
for name in greet_users(usernames).split(' ') :
    print("Hello, %s!" %name)