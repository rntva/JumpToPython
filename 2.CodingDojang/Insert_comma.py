def insert_comma(number) :
    number_copy = ""
    if number.find('.') != -1 :
        find_dot = number.find('.')
        for x in number[find_dot+1:] :
            number_copy += x
        number_copy += '.'
    else : find_dot = len(number)
    dot_count = 1
    for x in range(find_dot) :
        if dot_count % 3 == 0 :
            number_copy += number[find_dot - x - 1]
            number_copy += ','
        else : number_copy += number[find_dot - x - 1]
        dot_count += 1
    return number_copy

def reversed_print(number) :
    for x in range(len(number)) :
        print(number[len(number) - x - 1], end = '')

reversed_print(insert_comma("10200002120.333"))
