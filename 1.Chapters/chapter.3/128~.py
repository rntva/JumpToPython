# a = 1
# while a :
#     if a % 2 == 0 : print(a)
#     a += 1

# while True :
#    print("Ctrl + C를 눌러야 While문을 빠져나갈 수 있습니다.")

# for x in range(2,10) :
#     for y in range(1,10) :
#         print("%d * %d = %d" %(x, y, x*y), end='')
#     print()

# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for x in range(len(A)):
#     total += A[x]
# average = total / (x+1)
# print(average)
#
# num = 1
# for x in A :
#     if x >= 60 :
#         print("%d번 학생 Pass" %num)
#     else : print("%d번 학생 Fail" %num)
#     num += 1

x = 1
while x <= 5 :
    print('*' * x)
    x += 1

i = 0
while 1 :
    i += 1
    if i > 5 : break
    print('*' * i)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for x in A :
    total += x
print( total / len(A))

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for x in range(len(A)) :
    total += A[x]
    average = total / len(A)
print(average)