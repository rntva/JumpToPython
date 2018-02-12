# import sys
#
# args = sys.argv[1:]
# for x in range(10) :
#     if x > 5 : sys.exit()
#     else : print(args)
#
# print("\n-----------------------------------------------------")
#
# import pickle
#
# file1 = open("sample.txt", 'wb')
# data = {1 : 'python', 2 : 'jump to'}
# pickle._dump(data, file1)
# file1.close()
#
# file2 = open("sample.txt", 'rb')
# print(file2.readline())
# file2.seek(0)
# a = file2.readline()
# print(type(a))
# print(a)
#
# print("\n-----------------------------------------------------")
#
# import random
#
# # print(random.random())
#
# def random_pop(list) :
#     number = random.randint(0, len(list) - 1)
#     return list.pop(number)
#
# data = [1,2,3,4,5]
# while data : print(random_pop(data))
# print()
#
# data = [1,2,3,4,5]
# print(random.choice(data))
# print(data)
# print()
#
# random.shuffle(data)
# print(data)
#
# print("\n-----------------------------------------------------")
#
import webbrowser

webbrowser.open("www.google.com")
