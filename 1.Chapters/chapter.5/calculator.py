class Calculator :
    result = 0

    def __init__(self, list) :
        self.c_list = list[:]

    def sum(self) :
        for x in self.c_list :
            self.result += int(x)
        print(self.result)

    def avg(self) :
        self.result /= len(self.c_list)
        print(self.result)

if __name__ == "__main__" :
    cal1 = Calculator([1,2,3,4,5])
    cal2 = Calculator([6,7,8,9,10])

    cal1.sum()
    cal1.avg()
    cal2.sum()
    cal2.avg()
