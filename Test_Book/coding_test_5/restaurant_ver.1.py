class Restaurant :

    def __init__(self, input_name, input_cusine_type) :
        self.name = input_name
        self.cusine_type = input_cusine_type

    def describe_restaurant(self) :
        print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다." %(self.name, self.cusine_type))

    def open_restaurant(self) :
        print("저희 %s 레스토랑이 오픈했습니다." %self.name)


input_name, input_cusine_type = input("두근두근 레스토랑 타이군!!!\n\
레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split(' ')

First_restaurant = Restaurant(input_name, input_cusine_type)
print()
First_restaurant.describe_restaurant()
First_restaurant.open_restaurant()