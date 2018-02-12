class Calculator :
    def __init__(self, list):
        self.num_list = list[:]
        self.result = 0

    def sum(self):
        for x in self.num_list:
            self.result += x
        print(self.result)

    def avg(self):
        print(self.result/len(self.num_list))

if __name__ == "__main__" :
    cal1 = Calculator([1,2,3,4,5])
    cal1.sum()
    cal1.avg()
    cal2 = Calculator([6,7,8,9,10])
    cal2.sum()
    cal2.avg()
