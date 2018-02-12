class Restaurant_main :
    Mother_name = "요리왕비룡이직접런칭한한둘이먹다셋이죽어도모르는프렌차이즈레스토랑시리즈"

    def __init__(self, input_name, input_number) :
        self.name = input_name
        self.numbering = input_number

    # def describe_restaurant(self) :
    #     print("저희 레스토랑 명칭은 %s 이고 %s 전문점입니다." %(self.name, self.cusine_type))

    def open_restaurant(self) :
        print("저희 %s 레스토랑이 오픈했습니다." %self.name)

class Chinese_Restaurant(Restaurant_main) :

    def describe_restaurant(self) :
        print("%s 중국집 버전 %d번째 레스로토랑 %s입니다." %(self.Mother_name, self.numbering, self.name))

    def strong_point(self) :
        print("저희집은 3인분 이상 시키면 군만두가 써비스로 나갑니다.")

class Italian_restaurant(Restaurant_main) :

    def describe_restaurant(self) :
        print("%s 이탈리아 버전 %d번째 레스로토랑 %s입니다." %(self.Mother_name, self.numbering, self.name))

    def set_table(self, num) :
        print("%d명 오셨다. 테이블 세팅해라~!" %num)

# input_name, input_cusine_type = input("두근두근 레스토랑 타이군!!!\n\
# 레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split(' ')


china = Chinese_Restaurant("띵호와", 1)
china.describe_restaurant()
italia = Italian_restaurant("까르뻬딸라뇨", 2)
italia.describe_restaurant()
china.open_restaurant()
italia.open_restaurant()
china.strong_point()
italia.set_table(7)
