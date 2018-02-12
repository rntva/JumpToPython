def search_visitor(list, str) :
    for x in list.split(' ') :
        if x == str :
            print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요." %str)
            return 0

    return 1

file1 = open("방명록.txt", 'r')
file2 = open("방명록.txt", 'a')
while 1 :
    file1.seek(0)
    name = input("이름을 입력하세요.(종료는 '-1') : ")
    if name == '-1' : break
    name_str = file1.read()
    name_list_temp = name_str.split('\n')
    name_list = ""
    for x in name_list_temp :
        temp = str(x).split(' ')
        name_list += str(temp[0]) + ' '
    name_list = name_list[:-1]



    if search_visitor(name_list, name) == 1 :
        privacy = input("생년월일을 입력하세요. : ")
        print("%s씨의 첫 방문을 축하합니다." %name)
        file2.write('\n' + name + ' ' + privacy)
        file2.close()
        file2 = open("방명록.txt", 'a')

file1.close()
file2.close()
