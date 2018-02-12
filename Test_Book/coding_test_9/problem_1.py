while 1 :
    input_num = input("출력하고 싶은 단을 입력하십시오.(-1:종료, all:구구단 전체 출력) : ")
    if input_num == "all" :
        # Version_1
        # result = []
        # for y in range(2,10) :
        #     result = list(map(lambda x: x * y, range(1, 10)))
        # for y in range(2, 10):
        #     for z in range(9) : print("%d * %d = %d" %(y, z+1, result[z]))
        #------------------------------------------------------------------------------
        #Version_2
        # for x in range(2, 10) :
        #     for y in range(1, 10) :
        #         print("%d * %d = %d" %(x, y, x*y))
        # Version_3
        result = []
        for y in range(2, 10):
            result += list(map(lambda x: x * y, range(1, 10)))

        for x in range(1, 10) :
            index = x - 1
            for y in range(2, 10) :
                print("%d * %d = %-10d" %(y, x, result[index]), end = '')
                index += 9
            print()
    try :
        if int(input_num) != -1 and int(input_num) < 0 :
            raise ValueError
    except :
        print("음수가 들어왔습니다.")
        continue
    if input_num == "-1" : break

    else :
        result = list(map(lambda x : x * int(input_num), range(1,10)))
        for x in range(1,10) :
            print("%s * %d = %d" %(input_num, x, result[x-1]))

