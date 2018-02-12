while 1 :
    try :
        start_num, end_num = input("수의 범위를 입력하시오.(','로 구분) : ").split(',')
        start_num, end_num = int(start_num), int(end_num)
        counting_coin = int(input("어떤 숫자가 몇개 들었는지 카운팅 하고싶은가. : "))

        count = 0
        for x in range(start_num,end_num) :
            temp = str(x)
            temp = list(temp)
            for y in temp :
                if counting_coin == int(y) : count += 1

        print("%d부터 %d사이에 %d는 %d개 들어가있다." %(start_num, end_num, counting_coin, count))

        end_command = input("끝내고 싶다면 따라 쓰시오.\nLet me go.\n")
        if end_command == "Let me go." : break

    except :
        print("숫자만 입력 하시오.\n")

