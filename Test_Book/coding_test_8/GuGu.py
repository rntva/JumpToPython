input_number = int(input("출력한 구구단의 단을 입력해주세요. : "))

result_list = []
for x in range(1,10) : result_list.append(x * input_number)
print(result_list)