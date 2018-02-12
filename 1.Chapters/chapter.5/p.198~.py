# class Housepark :
#     lastname = "박"
#
# pey = Housepark()
# print(pey.lastname)
# Housepark.lastname = "창씨개명" #클래스의 요소를 그대로 받았을 때는 클래스의 요소가 바뀌면 자식들도 자동으로 바뀜
# pes = Housepark()
# print(pes.lastname)
# print((pey.lastname))
# pey.lastname = "박" #직접 값을 때려박으면 바뀌지 않음
# print(pes.lastname)
# print((pey.lastname))
# Housepark.lastname = "창씨개명"
# print((pey.lastname))

class Housepark :
    lastname = '박'

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, destination):
        self.destination = destination
        print("%s은(는) %s로 여행을 가고싶다" %(self.fullname, destination))

    def __add__(self, other):
        print("%s과 %s은(는) 각자의 여행지 %s와 %s에서 텔레파시로 의사소통을 했다." \
              %(self.fullname, other.fullname, self.destination, other.destination))

    def __sub__(self, other):
        print("%s과 %s은(는) 만나가다 성격차이로 헤어졌다네." \
              %(self.fullname, other.fullname))


pey = Housepark("응용")
print(pey.fullname)
pey.travel("안드로메다")

class HouseKim(Housepark) :
    lastname = "김"

    def travel(self, destination, days):
        self.destination = destination
        print("%s은(는) %s로 %d일 동안 여행을 가고싶어 한다." %(self.fullname, destination, days))

pes = HouseKim("줄리엣")
pes.travel("깐따삐아", 5)

pey + pes

pey - pes
