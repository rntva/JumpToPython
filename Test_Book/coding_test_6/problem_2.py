counting = 1
while 1 :
    name_input = input("안녕하세요. 이름을 입력하세요. : ")

    if counting > 3 and counting <= 10 :
        print("Hi %s!! You are %dth person come here!" %(name_input, counting))
    elif counting == 1 : print("Hi %s!! You are 1st person come here!" %name_input)
    elif counting == 2 : print("Hi %s!! You are 2nd person come here!" %name_input)
    elif counting == 3 : print("Hi %s!! You are 3rd person come here!" %name_input)
    else : print("Sorry %s. The event is closed because you are %dth person who come here"\
                 %(name_input, counting))

    counting += 1