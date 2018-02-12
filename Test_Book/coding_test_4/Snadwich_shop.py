def input_ingredient() :
    ing_str = ""
    while 1 :
        a = input("안녕하세요. 원하시는 재료를 입력하세요. : ")
        if a == "종료" :
            ing_list = ing_str.split(' ')
            ing_list = ing_list[:-1]
            return  ing_list
        else :
            ing_str += a + ' '

def make_sandwiches(ingredients) :
    print("샌드위치를 만들겠습니다.")
    for x in ingredients :
        print("%s를 추가합니다." %x)

order = input("안녕하세요. 저희 가게에 방문해 주셔서 갑사합니다.\n1.주문\n2.종료\n  입력 : ")
if order == "주문" :
    kitchen = input_ingredient()
    make_sandwiches(kitchen)
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")