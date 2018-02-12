while 1 :
    age_input = input("보통극장에 오신걸 환영합니다.\n나이를 말씀해 주십시오.(close입력시 마감) : ")

    if age_input == "close" : break

    try :
        age_input = int(age_input)
        if age_input < 3 : print("영유아는 무료입니다.\n")
        elif age_input >= 3 and age_input <= 12 : print("어린이는 10달러입니다.\n")
        else : print("청소년이상은 15달러입니다.\n")
    except ValueError : print("close가 아니라면 숫자만 입력해주십시오.\n")