class Restaurant :

    def __init__(self, input_name, input_cusine_type) :
        self.name = input_name
        self.cusine_type = input_cusine_type
        self.number_served = 0

    def describe_restaurant(self) :
        print("\n저희 레스토랑 명칭은 %s이고 %s 전문점입니다." %(self.name, self.cusine_type))

    def open_restaurant(self) :
        print("\n저희 %s 레스토랑이 오픈했습니다." %self.name)

    def set_numver_served(self) :
        self.number_served = 0
        print("\n손님 카운팅을 0으로 초기화 하였습니다.")

    def increment_number_served(self, input_customer) :
        self.number_served += input_customer
        print("손님 %d명 들어오셨고 지금까지 총 %d명 오셨습니다." %(input_customer, self.number_served))

input_name, input_cusine_type = input("두근두근 레스토랑 타이군!!!\n\
레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split(' ')

First_restaurant = Restaurant(input_name, input_cusine_type)
First_restaurant.describe_restaurant()

open_close = input("\n장사를 시작하려면 오픈을 입력하시오. 문 닫으려면 마감. :")
if open_close == "오픈" :
    First_restaurant.open_restaurant()
    while 1 :
        input_customer = input("\n어서오세요. 몇명이십니까?(초기화하려면 0입력) : ")
        if input_customer == "마감" : break
        elif input_customer == '0' : First_restaurant.set_numver_served()
        else :
            print("\n주문 받고 나가고 어쩌고……")
            First_restaurant.increment_number_served(int(input_customer))
else : print("다 제끼고 놀자~")

