#이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌
while 1 :
    try :
        input_string = input("\n이름을 ','로 구분하여 입력하시오.(종료를 원하면-1입력) : ")
        if input_string == '-1' : break
        # dummy_input_string = input_string[:]
        dummy_input_string = ""
        dummy_input_string_list = []
        family_name = []
        name_in = ""
        do_once = 1
        for x in input_string : #성만 뽑아내기
            if do_once == 1 :
                family_name.append(x)
                do_once = -1
            elif x == ',' :
                do_once = 1
        dummy_family_name = family_name[:] #원본은 남겨두자

        print("")
        while 1 : #성씨 별로 몇 명 있나 출력.
            x = 0
            temp = dummy_family_name.count(dummy_family_name[x])
            print("%s씨는 %d명이다 나왔다." %(dummy_family_name[x], dummy_family_name.count(dummy_family_name[x])))
            temp_famil_name = dummy_family_name[x]
            while 1 :
                if temp_famil_name in dummy_family_name :
                    dummy_family_name.remove(temp_famil_name)
                else : break
            if len(dummy_family_name) > x : x += 1
            else : break

        search_name = input("\n이름이 몇 개가 중복되는지 찾아보자. : ")
        print("%s란 이름이 %d명이 있다" % (search_name, input_string.count(search_name)))

        print("\n중복을 제거하고 이름을 출력하자.")
        for x in input_string : #중복 제거 후 이름 출력
            coin = 1
            if x != ',' :
                name_in += x
                coin = 0
            elif coin == 1 :
               if name_in not in dummy_input_string :
                   dummy_input_string += name_in
                   dummy_input_string += ','
               name_in = ""
        dummy_input_string = str(dummy_input_string[:-1])
        print(dummy_input_string)

        print("\n중복을 제거한 이름들을 오름 차순으로 출력하자")
        dummy_input_string_list = dummy_input_string.split(',')
        dummy_input_string_list = sorted(dummy_input_string_list)
        print(dummy_input_string_list)

    except : print("오류남.")



