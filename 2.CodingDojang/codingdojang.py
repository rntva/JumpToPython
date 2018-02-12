# # 3, 5의 배수들의 총 합
# #내 코드
# result = 0
# for x in range(1,1000) :
#     if x % 3 == 0 or x % 5 == 0 :
#         result += x
# print(result)
# #한줄짜리
# print(sum(list([x for x in range(1000) if x%3==0 or x%5==0])))
#
# #range(1,5000)에서 셀프 넘버들의 합
# #내 코드
# number_set1 = set()
# number_set2 = set()
# result = 0
# for x in range(1,5000) :
#     number_set1.add(x)
# for x in range(1,5000) :
#     temp = 0
#     temp = int(x / 1000) + int((x % 1000 / 100)) + int((x % 100 ) / 10) + int(x % 10) + x
#     number_set2.add(temp)
# result_set = number_set1 - number_set2
# print(sum(result_set))
# #한줄짜리
# print(sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))

# #range(1,10000)에서 8이 총 몇 번 나오는가?
# #내 코드
# eight_counting = 0
# string = ""
# for x in range(1,10000) :
#     string = str(x)
#     for y in string :
#         if y == "8" : eight_counting += 1
# print(eight_counting)
#
# #한줄짜리
# print(str(list(range(1, 10001))).count('8')) #.count라는 멤버함수를 깜빡했다.

# #1차원의 점들 사이 가장 가까운 것들의 쌍 출력
# arr_a = [1, 3, 4, 8, 13, 17, 20]
# temp = 0
# t_temp = 2 ** 31
# x_y = []
# for x in range(len(arr_a) - 1) :
#    temp = arr_a[x+1] - arr_a[x]
#    if temp < t_temp :
#         x_y = [x, x+1]
#         t_temp = temp
#    else : None
# print(arr_a[x_y[0]], arr_a[x_y[1]])

# #2차원 배열의 크기 지정하면 [0][0]부터 오른쪽으로 벽 타고 가면서 숫자 출력
# size = int(input("Set the volume of column and row: "))
# new_arr = []
# start_x = 0
# start_y = 0
# end_ux = 0
# end_dx = size
# end_ly = -1
# end_ry = size
# numbering = 0
#
# for x in range(size) :
#     new_arr.append([0] * size)
#
# for x in range(size*2-1) :
#     if x % 4 == 0 :
#         while start_y < end_ry :
#             new_arr[start_x][start_y] = numbering
#             numbering += 1
#             if numbering == size * size : break
#             start_y += 1
#         end_ry -= 1
#         start_y -= 1
#         start_x += 1
#     elif x % 4 == 1 :
#         while start_x < end_dx:
#             new_arr[start_x][start_y] = numbering
#             numbering += 1
#             if numbering == size * size : break
#             start_x += 1
#         end_dx -= 1
#         start_x -=1
#         start_y -= 1
#     elif x % 4 == 2 :
#         while start_y > end_ly :
#             new_arr[start_x][start_y] = numbering
#             numbering += 1
#             if numbering == size * size : break
#             start_y -= 1
#         end_ly += 1
#         start_y += 1
#         start_x -= 1
#     elif x % 4 == 3 :
#         while start_x > end_ux :
#             new_arr[start_x][start_y] = numbering
#             numbering += 1
#             if numbering == size * size : break
#             start_x -= 1
#         end_ux += 1
#         start_x += 1
#         start_y += 1
#
# for x in range(size) :
#     for y in range(size) :
#         print("%3d" %new_arr[x][y], end = '')
#     print('')

# #문자열 받아서 한 문자가 몇 개 나왔나 카운팅하기
# input_str = input("문자열을 입력하십시오. : ")
# input_str_index = 0
# input_string_count = 0
# output_str = []
# for x in input_str :
#     input_string_count = input_str.count(input_str[input_str_index])
#     if x not in output_str :
#         output_str.append(input_str[input_str_index])
#         output_str.append(input_string_count)
#     # for x in range(input_string_count) :
#     #     input_str.replace(input_str[input_str_index], '')
#     input_str_index += 1
#     try :
#         1
#     except :
#         break
# for x in output_str :
#     print(x, end='')

# #3n+1 Problem
# while 1 :
#     start_num = int(input("Input starting number: "))
#     end_num = int(input("Input ending number: "))
#     output_value = 0
#     temp_num = 0
#
#
#     for x in range(start_num, end_num) :
#         temp_num = x
#         temp_count = 0
#         while 1 :
#             if temp_num == 1:
#                 if output_value < temp_count :
#                     output_value = temp_count + 1
#                     # print(temp_num, end='')
#                     break
#                 else :
#                     break
#             else :
#                 if temp_num % 2 == 0 :
#                     temp_num /= 2
#                     temp_count += 1
#                     # print(temp_num, end='')
#                 else :
#                     temp_num = 3 * temp_num + 1
#                     temp_count += 1
#                     # print(temp_num, end='')
#     print(output_value)

#피보나치 수열
fib = int(input("Input number:"))

def f_fib(a) :
    if a == 0 :
        return 0
    elif a == 1 :
        return 1
    else :
        return f_fib(a- 2) + f_fib(a-1)
for x in range(fib) :
    print(f_fib(x), end=' ')

# #모든 짝수번째 숫자를 '*'로 치환하시오
# input_str = input("아무거나 쳐보세요. : ")
# str_to_list = []
# for x in input_str :
#     str_to_list.append(x)
# for x in range(len(str_to_list)) :
#     # if (x+1) % 2 == 0 and '0' <= str_to_list[x] and str_to_list[x] <= '9' :
#     #     str_to_list[x] = '*'
#     if (x+1) % 2 == 0 :
#         try :
#             int(str_to_list[x])
#             str_to_list[x] = '*'
#         except ValueError : None
# print(str_to_list)

# #Insertion Sort
# def switch_position(arr1, index1, index2) : #index1이 비교 주체 index2가 비교 대상
#     value = 0
#     while 1:
#         if arr1[index2] > arr1[index1] and index2 > 0 :
#             value = index2
#             index2 -= 1
#         elif arr1[index2] > arr1[index1] : return index2
#         elif index1 - index2 > 1 : return value
#         else : return -1
#         # elif arr1[index2] > arr1[index1] :
#         #     return index2
#         # else : return index2
#
#     # while 1 :
#     #     if arr1[index1] < arr1[index2] and index2 > 0:
#     #         index2 -= 1
#     #         continue
#     #     elif arr1[index1] < arr1[index2] :
#     #         temp1 = arr1[index1]
#     #     while index2 < index1 :
#     #         arr1[index1] = arr1[index1-1]
#     #         index1 -= 1
#     #     arr1[index2] = temp1
#     #     break
#     # return arr1
#
# # input_list = list(input("Make a list : "))
# input_list = [7,4,1,8,5,2,9,6,3,0,12,11,64,87,32,20,27,86,52,64,78,16,33]
# for x in range(1,len(input_list)) :
#     set_position = switch_position(input_list, x, x-1)
#     if set_position != -1 :
#         temp = input_list[x]
#         while set_position < x :
#             input_list[x] = input_list[x-1]
#             x -= 1
#         input_list[x] = temp
#     else : None
#
# print(input_list)

