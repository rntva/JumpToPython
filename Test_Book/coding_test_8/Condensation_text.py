input_string = input("문자열을 입력하면 압축해 드립니다. : ")

count = 1
temp = input_string[0]
for x in input_string[1:] :
    if temp == x :
        count += 1
        temp = x
    else :
        print("%s%d" %(temp,count), end = ' ')
        count = 1
        temp = x
print("%s%d" %(temp,count))