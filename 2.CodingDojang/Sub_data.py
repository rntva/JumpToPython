month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def split_date(string) :
    temp = string.split(' ')
    date_1 = temp[0]
    date_2 = temp[2]
    return date_1, date_2

def total_days(string_1, string_2) :
    total_1 = int(string_1[6:])
    total_2 = int(string_2[6:])

    for x in range(1, int(string_1[:4]) + 1) :
        if x % 4 == 0 : total_1 += 366
        elif x % 100 == 0 and x % 400 != 0 : total_1 -= 1
        else : total_1 += 365

    for x in range(1, int(string_2[:4]) + 1) :
        if x % 4 == 0 : total_2 += 366
        elif x % 100 == 0 and x % 400 != 0 : total_2 -= 1
        else : total_2 += 365

    for x in range(1, int(string_1[4:6]) + 1) :
        total_1 += month[x]
        if month[x] == 2 and int(string_1[:4]) % 4 == 0 and int(string_1[:4]) % 100 != 0 : total_1 += 1
        if int(string_1[:4]) % 400 == 0 : total_1 += 1

    for x in range(1, int(string_2[4:6]) + 1) :
        total_2 += month[x]
        if month[x] == 2 and int(string_2[:4]) % 4 == 0 and int(string_2[:4]) % 100 != 0 : total_2 += 1
        if int(string_2[:4]) % 400 == 0 : total_2 += 1

    return (total_1 -  total_2)


    # year_1 = int(string_1[:4])
    # month_1 = int(string_1[4:6])
    # day_1 =  int(string_1[6:])
    # year_2 = int(string_2[:4])
    # year_2 = int(string_2[4:6])
    # year_2 = int(string_2[6:])

a = "20070515 sub 20070501"
b = "20070501 sub 20070515"
c = "20070301 sub 20070515"

d = split_date(a)
print(total_days(str(d[0]), str(d[1])))
d = split_date(b)
print(total_days(str(d[0]), str(d[1])))
d = split_date(c)
print(total_days(str(d[0]), str(d[1])))