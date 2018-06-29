# import math
#
# def suger_delivery() :
#     total_suger = int(input("설탕 총 양 : "))
#     return_value = int(total_suger / 5)
#
#     if (total_suger % 5) / 3 == 0 :
#         return_value += int(total_suger / 5 / 3)
#
#     else : return_value = -1
#
#     print(return_value)
#
# def terret() :
#     test_case_num = int(input("테스트 케이스 숫자를 입력하십시오. : "))
#     input_pos_list = []
#     result_pos_list = []
#
#     for x in range(test_case_num) :
#         temp_pos_list = input("좌표 및 거리를 입력하십시오. : ").split(' ')
#         temp_pos_list = list(map(int, temp_pos_list))
#         input_pos_list.append(temp_pos_list)
#
#     for x in range(len(input_pos_list)) :
#         r1 = input_pos_list[x][4]
#         r2 = input_pos_list[x][5]
#         r3 = math.sqrt((input_pos_list[x][0] - input_pos_list[x][2]) * (input_pos_list[x][0] - input_pos_list[x][2]) + \
# (input_pos_list[x][1] - input_pos_list[x][3]) * (input_pos_list[x][1] - input_pos_list[x][3]))
#
#         if r3 == 0 :
#             print(0)
#
#         elif r1 < r3 and r2 < r3 :
#             if (r1 + r2) > r3 :
#                 print(0)
#             elif (r1 + r2) == r3 :
#                 print(1)
#             else :
#                 print(2)
#
#         elif r1 < r2 and r3 < r2 :
#             if (r3 + r2) > r2 :
#                 print(0)
#             elif (r3 + r2) == r2 :
#                 print(1)
#             else :
#                 print(2)
#
#         elif r2 < r1 and r3 <r1 :
#             if (r3 + r2) > r1 :
#                 print(0)
#             elif (r3 + r2) == r1 :
#                 print(1)
#             else :
#                 print(2)
#
#         else :
#             print(-1)
#
#     # print(len(input_pos_list))
#
# # suger_delivery()
# terret()
#
import tensorflow as tf
a = tf.Session()
hello = tf.constant('hello')
a.run(hello)
print(a.run(hello))

# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)