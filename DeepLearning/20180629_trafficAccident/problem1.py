import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_locaton = "C:\\Windows\\Fonts\\HMKMG.TTF"
font_name = font_manager.FontProperties(fname=font_locaton).get_name()
rc("font", family=font_name)

data_frame = pd.read_csv("도로교통공단_전국_사망교통사고_2017.csv", engine="python")

# VBD = {'일' : 0, '월' : 0, '화' : 0, '수' : 0, '목' : 0, '금' : 0, '토' : 0}
#
# day = list(data_frame["요일"])
# number = list(data_frame["사상자수"])
#
# for x in range(len(day)):
#     if number[x] >= 3 :
#         VBD[day[x]] += number[x]
#
# plt.style.use('ggplot')
#
# day_index = range(len(VBD.keys()))
# dieORhurt = list(VBD.values())
#
# fig = plt.figure()
# ax1 = fig.add_subplot(1, 1, 1)
# ax1.bar(day_index, dieORhurt, align="center", color="darkblue")
# ax1.xaxis.set_ticks_position("bottom")
# ax1.yaxis.set_ticks_position("left")
# plt.xticks(day_index, list(VBD.keys()), rotation=0, fontsize="small")
# # ax1.set_xticklabels(["", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"])
# plt.xlabel("요일")
# plt.ylabel("사상자수")
# plt.title("요일별 사상자수")
# plt.show()


rk_dic = {}

region_kyunggi = data_frame.loc[(data_frame["발생지시도"].str.contains("경기")) & data_frame["사망자수"] >= 1, : ]

# temp = region_kyunggi[["발생지시군구", "사망자수"]]
# print(temp)



rk_skg = list(region_kyunggi["발생지시군구"])
rk_dieNum = list(region_kyunggi["사망자수"])

for keys in set(rk_skg) :
    rk_dic[keys] = 0

for index in range(len(rk_skg)) :
    rk_dic[rk_skg[index]] += rk_dieNum[index]

sibal = { "발생지군구" : list(rk_dic.keys()),
          "사망자수" : list(rk_dic.values())}

print(sibal)
print(rk_dic)
# temp = pd.DataFrame(rk_skg, columns="발생지시군구")

# for key, value in rk_dic.items() :
#     temp.append(key, value)

# print(temp)

top_list = []
min = 0

# for key in rk_dic.keys() :
#     if len(top_list) >= 5 :
#         for pre in top_list :
#             if rk_dic[key] > rk_dic[pre] :
#                 top_list.remove(pre)
#                 top_list.append(key)
#
#     else :



