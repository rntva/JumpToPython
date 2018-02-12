import time

input_string = input("숫자형 문자열을 입력해주십시오.(다중 입력시 공백으로 구분) : ").split(' ')
counting = 0
for x in input_string :
    if 10 != len(input_string[counting]) :
        print("false", end = ' ')
    else :
        sorted_x = sorted(x)
        # token = 0
        for y in range(10) :
            if y != int(sorted_x[y]) :
                print("false", end = ' ')
                # token = 0
                break
            else : token = 1
    if token == 1 : print("true", end = ' ')
    counting += 1
    token = 0

# input_string = input("숫자형 문자열을 입력해주십시오.(다중 입력시 공백으로 구분) : ").split(' ')
for x in range(len(input_string)):
    if sorted(input_string[x]) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: print(True, end=' ')
    else: print(False, end=' ')


# input_string = input("숫자형 문자열을 입력해주십시오.(다중 입력시 공백으로 구분) : ").split(' ')
print(list(map(lambda x : sorted(x) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], input_string  )))
