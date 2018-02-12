def judge_common_multiple(catch_num_1, catch_num_2, catch_num_3) :
    if catch_num_3 % catch_num_1 == 0 and catch_num_3 % catch_num_2 == 0 :
        return "%d는 %d와 %d의 공배수입니다.\n" %(catch_num_3, catch_num_1, catch_num_2)
    else : return "%d는 %d와 %d의 공배수가 아닙니다.\n" %(catch_num_3, catch_num_1, catch_num_2)

while 1 :
    try :
        num_input_temp = input("숫자 3개를 입력해 주십시오.(종료는 -1) : ").split(' ')
        if num_input_temp[0] == '-1' : break
        num_1, num_2, num_3 = int(num_input_temp[0]), int(num_input_temp[1]), int(num_input_temp[2])
        print(judge_common_multiple(num_1, num_2, num_3))
    except ValueError : print("숫자만 입력하십시오.\n")