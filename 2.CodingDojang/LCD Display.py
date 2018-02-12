#LCD Display    #값 2개를 한 줄에 입력받을 때 : s, n = input().split(' ') 이런 식으로 한다.
def print_0(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*num2 + ' ')
    else : result.append('|'+' '*num2 + '|')

def print_1(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' '*(num2+2))
    else : result.append(' '*(num2+1) + '|')

def print_2(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*num2 + ' ')
    elif num1 < num2 + 1 : result.append(' '*(num2+1) + '|')
    else : result.append('|' + ' '*(num2+1))

def print_3(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*num2 + ' ')
    else : result.append(' '*(num2+1) + '|')

def print_4(num1, num2) :
    if num1 == 0 or num1 == 2*num2+2 : result.append(' '*(num2+2))
    elif num1 < num2 + 1 : result.append('|' + ' ' * num2 + '|')
    elif num1 == num2+1 : result.append(' ' + '-'*num2 + ' ')
    else : result.append(' '*(num2+1) + '|')

def print_5(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*num2 + ' ')
    elif num1 < num2 + 1 : result.append('|' + ' '*(num2+1))
    else : result.append(' '*(num2+1) + '|')

def print_6(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*num2 + ' ')
    elif num1 < num2 + 1 : result.append('|' + ' '*(num2+1))
    else : result.append('|' + ' '*num2 + '|')

def print_7(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*(num2) + ' ')
    elif num1 < num2 + 1 : result.append('|' + ' '*num2 + '|')
    else : result.append(' '*(num2+1) + '|')

def print_8(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*(num2) + ' ')
    else : result.append('|' + ' '*num2 + '|')

def print_9(num1, num2) :
    if num1 == 0 or num1 == num2+1 or num1 == 2*num2+2 : result.append(' ' + '-'*(num2) + ' ')
    elif num1 < num2 + 1 : result.append('|' + ' '*num2 + '|')
    else : result.append(' '*(num2+1) + '|')

num = []
result = []
c = input("S값 : , 숫자 : ").split(' ')
y = int(c[0])
temp = list(c[1])
for x in range(len(temp)) :
    num.append(int(temp[x]))

for xx in range(len(temp)) :
    for x in range(2*y+3) :
        if temp[xx] == '0' : print_0(x, y)
        if temp[xx] == '1' : print_1(x, y)
        if temp[xx] == '2' : print_2(x, y)
        if temp[xx] == '3' : print_3(x, y)
        if temp[xx] == '4' : print_4(x, y)
        if temp[xx] == '5' : print_5(x, y)
        if temp[xx] == '6' : print_6(x, y)
        if temp[xx] == '7' : print_7(x, y)
        if temp[xx] == '8' : print_8(x, y)
        if temp[xx] == '9' : print_9(x, y)

for x in range(2*y+3) :
    while 1 :
        if x >= len(result) :
            print()
            break
        else :
            print(result[x], end=' ')
            x = x + (2*y+3)