input_numbers = input("범위, 첫 번째수, 두 번째수를 입력하세요.(종료 : 프로그램종료) : ").split(' ')

for x in range(3) : input_numbers[x] = int(input_numbers[x])
multiplies_1 = list(filter(lambda x : x % input_numbers[1] == 0, range(1,input_numbers[0]+1)))
multiplies_2 = list(filter(lambda x : x % input_numbers[2] == 0, range(1,input_numbers[0]+1)))
set_mul1_mul2 = sorted(set(multiplies_1 + multiplies_2))
print("0부터 %d이하의 범위를 선택하셨습니다. 이 중에서" %input_numbers[0])
print("%d의 배수는 " %input_numbers[1], end = '')
print(multiplies_1, end = '')
print("입니다.\n%d의 배수는 " %input_numbers[2], end = '')
print(multiplies_2, end = '')
print("입니다.\n%d와 %d의 배수는 ", end = '')
print(set_mul1_mul2)
print("따라서 0부터 %d이하의 범위%d와 %d의 배수의 총합은 %d입니다."\
%(input_numbers[0], input_numbers[1], input_numbers[2], sum(set_mul1_mul2)))