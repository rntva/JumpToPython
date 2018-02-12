def show_list(list) :
    for x in list :
        print(x)

def make_idol(list) :
    for x in list :
        print("신예 아이돌 %s 인기 급상승" %x)

def make_world_star(list) :
    for x in list :
        print("아이돌 %s 월드스타 등극" %x)

file1 = open("연습생.txt", 'r', encoding='UTF8')
Idol_str = file1.read()
Idol_list = Idol_str.split('\n')
show_list(Idol_list)
make_idol(Idol_list)
make_world_star(Idol_list)

file1.close()
