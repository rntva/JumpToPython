class Service :
    secret = "영구는 배꼽이 2개다."

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %d + %d = %d입니다." %(self.name, a, b, result))

    def __del__(self):
        print("이용해 주셔서 감사합니다.")

pey = Service("홍길동")
pey.sum(3, 4)