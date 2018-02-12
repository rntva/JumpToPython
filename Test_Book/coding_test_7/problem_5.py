def sum(int_1, int_2) :
    return int_1 + int_2

def substractor(int_1, int_2):
    return int_1- int_2

def multiplier(int_1, int_2):
    return int_1 * int_2

def divisioner(int_1, int_2):
    try : return int_1 / int_2
    except ZeroDivisionError : return "두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되면 안됩니다."

while 1:
    again = 0
    num_input = input("안녕하세요. 두 수를 입력하세요.(종료: 프로그램종료) : ").split(' ')
    if num_input[0] == "종료" : break
    else :
        for x in range(len(num_input)) :
            try :
                num_input[x] = int(num_input[x])
            except ValueError :
                again = 1
                print("죄송합니다. %d번째 숫자가 '%s'입니다. 숫자를 입력하세요.\
" %(x+1, num_input[x]))
        if again == 1 : continue
        print(sum(num_input[0], num_input[1]))
        print(substractor(num_input[0], num_input[1]))
        print(multiplier(num_input[0], num_input[1]))
        print(divisioner(num_input[0], num_input[1]))