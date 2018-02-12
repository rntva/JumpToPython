def sum(a, b) :
    return a + b

def sum_safe(a, b) :
    if type(a) != type(b) :
        re_str = "연산할 수 없습니다."
        return re_str
    else :
        return a + b

if __name__ == "__main__" :
    print(sum(3,5))
    print(sum_safe(8,'a'))