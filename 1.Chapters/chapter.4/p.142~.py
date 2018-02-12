def init() :
    print("시작이다!")

# def sum(a, b) :
#     if a >= 0 and b >= 0 : print("%d + %d = %d" %(a, b, a+b))
#     else : print("자연수만 입력하시오.")
#     return 0

def sum(arry) :
    result = 0
    for x in arry :
        temp = int(x)
        if temp >= 0 :
            result += temp
        else : print("자연수만 입력하시오.")
    return result

# def sum_and_mul(a, b) :
#     if a >= 0 and b >= 0 :
#         sum_result = a +b
#         mul_result = a * b
#     else : print("자연수만 입력하시오.")
#     return sum_result ,mul_result

def sum_and_mul(arry) :
    result_sum = 0
    result_mul = 1
    for x in arry :
        temp = int(x)
        if temp >= 0 :
            result_sum += temp
            result_mul *= temp
        else : print("자연수만 입력하시오.")
    return result_sum, result_mul

while 1 :
    try :
        init()
        arry = input("값을 입력하십시오.(공백으로 구분, 종료는 문자열) :").split(' ')
        # x, y = input("값을 2개 입력하십시오.(공백으로 구분, 종료는 문자열) :").split(' ')
        # x, y = int(x), int(y)
        print(sum(arry))
        print(sum_and_mul(arry))
        temp_sum_and_mul = sum_and_mul(arry)
        print("더하기는 : %d\n곱하기는 : %d" %(temp_sum_and_mul[0], temp_sum_and_mul[1]))
    except :
        print("종료.")
        break
