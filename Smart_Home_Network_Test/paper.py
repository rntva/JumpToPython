import time
import threading
import urllib.request
from bs4 import BeautifulSoup
import json
import signal
import os
import subprocess

# class function_for_test_threaging(threading.Thread) :
#     def __init__(self) :
#         threading.Thread.__init__(self)
#         self.stop = threading.Event()
#         self.daemon == True
#
#     def run(self) :
#         for x in range(20) :
#             print(x)
#             time.sleep(0.1)
#
#     def stop(self) :
#         self.stop.set()
#
#     def go_again(self) :
#         self.stop.clear()
#
# # t = threading.Thread(target=function_for_test_threaging)
# # t.daemon = True
# # t.start()
# # k = threading.Event()
#
# # c = t.getName()
# # print(c)
# # print(threading.get_ident())
# #
# # print(os.getpid())
#
# th = function_for_test_threaging()
# th.start()
#
# for x in range(20) :
#     print("%d번째 출력." %x)
#     if x == 10 : th.stop()
#     elif x == 15 : th.go_again()
#     time.sleep(0.1)

# test_url = "http://openapi.safekorea.go.kr/openapi/service/behaviorconductKnowHow/naturaldisaster/list?safety_cate=01001&serviceKey=DthpXT7YzG6wllvd7zn6DyNRVJJGmVR2EGEs5UWg%2BeVXHyMkw%2FxNO2WcSwTZc9RX0sJzCK5d3bNOxD16Etj0%2Fg%3D%3D&"
# req = urllib.request.Request(test_url)
#
#
# try :
#     response_1 = urllib.request.urlopen(test_url)
#     retData = response_1.read().decode("utf-8")
#     print("Successed")
# except Exception as e :
#     print(e)
#     print("Failed")
# temp_5 = []
# temp_1 = retData.split('<meta property="og:description" content=\"')
# temp_2 = temp_1[1].split('\"')[0]

# get_door_contorl_signal = soupData.findAll("meta")
# print(temp_2)
# print(temp_3)

# g_disaster = {"01001" : "태풍", "01002" : "홍수", "01003" : "호우", "01004" : "강풍", "01005" : "대설", "01006" : "한파", "01007" : "풍랑",
#               "01008" : "황사", "01009" : "폭염", "01010" : "가뭄", "01011" : "지진", "01012" : "지진해일", "01013" : "해일",
#               "01014" : "산사태", "01015" : "화산폭발"}
#
# c = list(g_disaster.keys())
# print(type(c[0]))

url = "https://m.blog.naver.com/PostList.nhn?permalink=permalink&blogId=calmstalker"
temp_dic = {}

try:
    response_1 = urllib.request.urlopen(url)
    retData = response_1.read().decode("utf-8")
    print("Successed")
except Exception as e:
    print(e)
    print("Failed")

temp_1 = retData.split('<meta property="og:description" content=\"')
temp_2 = temp_1[1].split('\"')[0].split(',')
for x in temp_2 :
    splited_x = x.split(':')
    temp_dic[splited_x[0]] = splited_x[1]

print(temp_dic)