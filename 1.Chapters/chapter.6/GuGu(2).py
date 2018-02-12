def gugu(list, num) :
    for x in range(1, 10) :
        list.append(x*num)
    return list

list = []
gugu(list, 3)
print(list)