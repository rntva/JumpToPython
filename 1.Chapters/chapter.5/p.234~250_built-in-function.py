# x = 2
# y = 3
# z = 5
# print(all([x > 1, y > 0 , z == 5]))
# print(all([x > 1, y < 0 , z == 5]))
# print(any([x > 1, y < 0 , z == 5]))
#
# print("-----------------------------------------------------")
#
# print(dir(1))
# print(dir('a'))
# print(dir([1,2,3]))
# print(dir({1,2,3}))
#
# print("-----------------------------------------------------")
#
# print(divmod(z,2))
#
# print("-----------------------------------------------------")
#
# names = ["이유덕","이재영","권종표","이재영","박민호"]
# for a, name in enumerate(names) :
#     print("names[%d] : %s" %(a, name), end=' ')
#
# print("\n-----------------------------------------------------")
#
# a = '1'
# aa = '+'
# b = '2'
# print(eval(a+aa+b))
#
# print("\n-----------------------------------------------------")
#
# def posit_num(list) :
#     result = []
#     for x in list :
#         if x > 0 : result.append(x)
#     return result
# print(posit_num([1,2,-3,4,-5,-6]))
#
#
# def posit_filter(list) :
#     return list > 0
# print(list(filter(posit_filter, [1,2,-3,4,-5,-6])))
#
# print("\n-----------------------------------------------------")
#
# class Person() :
#     def __init__(self):
#         print("사람이다.")
#
# a = Person()
# print(isinstance(a, Person))
#
# print("\n-----------------------------------------------------")
#
# list = [lambda a, b : a+b, lambda a, b : a * b]
# for x in range(1,10) :
#     print(list[0](x, x+1), end=' ')
# print('/////', end=' ')
# for x in range(1,10) :
#     print(list[1](x, x+1), end=' ')
# print()
#
# list_a = filter(lambda x: x > 0, [1,2,-3,-4,-5,6,7,-8])
# print(filter(lambda x: x > 0, [1,2,-3,-4,-5,6,7,-8]))
# print(list_a)
# print("%s" %list_a)
# for x in list_a : print(x, end=' ')
# print()
#
# list_b = map(lambda  a : a*2,[1,2,3,4])
# print(map(lambda  a : a*2,[1,2,3,4]))
# print(type(list_b))
# for x in list_b : print(x, end=' ')
# print()
#
# print("\n-----------------------------------------------------")
#
print(chr(97))
print(ord('A'))
print(pow(2,3))
print(pow(2,3,3))
for x in range(1,10,2) :
    print(x, end=' ')
print()
str = ['가','다','라','하','마','바','차','나']
print(sorted(str))
temp = zip([1,2,3],[4,5,6,],[7,8,9])
print(type(temp))
print(temp)