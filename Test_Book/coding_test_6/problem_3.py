def judge_10(num_catch) :
    if num_catch % 10 == 0 : return "이것은 10의 배수가 맞습니다.\n"
    else : return "이것은 10의 배수가 아닙니다.\n"

while 1 :
    try :
        num_input = int(input("자연수를 입력해 주십시오.(종료는 -1) : "))
        if num_input == 0 or num_input < -1 : print("자연수 입력하라고 했잖아!\n")
        elif num_input == -1 : break
        else :
            print(judge_10(num_input))

    except ValueError : print("숫자만 입력하십시오.\n")


