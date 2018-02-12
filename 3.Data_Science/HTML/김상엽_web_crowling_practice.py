# import urllib.request
# from bs4 import BeautifulSoup
# from pandas import DataFrame
# import time
# import xml.etree.ElementTree as ET
#
# def time_change_to_str() :
#     now = ""
#     get_now = time.ctime().split(' ')
#     get_now_time = get_now[3].split(':')
#     for x in get_now[:3] : now += x
#     for x in get_now_time : now += x
#     now += get_now[-1]
#     return now
#
# html = urllib.request.urlopen("http://www.saramin.co.kr/zf_user/jobs/public/list/page/1?sort=ud&listType=public&public_list_flag=y#searchTitle")
# # xml = html.read().decode("UTF-8")
# # root = ET.fromstring(xml)
# soupData = BeautifulSoup(html, "html.parser")
#
# title_tag = soupData.findAll('a', attrs = {"str_tit"}) #타이틀 따기
# title_list = []
# for x in title_tag[:200] :
#     title_list.append(x.string)
#
# job_sector_tag = soupData.findAll('div', attrs = {"job_sector"})
# job_sector_list = []
# # k = job_sector_tag[0].text[1:] /job_sector 따기
# for x in job_sector_tag[:100] :
#     job_sector_list.append(x.text[1:])
#
# recruit_condition_tag = soupData.findAll('td', attrs = {"recruit_condition"}) #학력 따기
# recruit_condition_list = []
# for x in recruit_condition_tag[:100] :
#     temp = ""
#     for y in list(x.text[1:]) :
#         if y == '\n' : temp += '_'
#         else : temp += y
#     recruit_condition_list.append(temp)
#
# company_info_tag = soupData.findAll('td', attrs = {"company_info"}) #회사 정보 따기
# company_info_list = []
# for x in company_info_tag[:100] :
#     temp = ""
#     # q = x.text.split('\n')
#     for y in x.text.split('\n') :
#         if y != '' : temp += y
#         else : pass
#     company_info_list.append(temp)
#
# deadlines_tag = soupData.findAll('p', attrs = "deadlines")
# deadlines_list = []
# for x in deadlines_tag :
#     deadlines_list.append(x.text)
#
# result = []
# for x in range(100) :
#     result.append([title_list[2*x] + title_list[2*x+1]] + [job_sector_list[x]] + [recruit_condition_list[x]] +\
# [company_info_list[x]] + [deadlines_list[x]] )
#
# saramin_table = DataFrame(result, columns = ("Job Title", "Job Sector", "Recruit Condition", "Company Info",\
# "DeadLines_" + time_change_to_str()))
# saramin_table.to_csv("1000대기업 공채속보.csv", encoding="cp949", mode='w', index=True)
#
# print("End")

import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import time
import os
# import xml.etree.ElementTree as ET

def time_change_to_str() :
    now = ""
    get_now = time.ctime().split(' ')
    get_now_time = get_now[3].split(':')
    for x in get_now[:3] : now += x
    for x in get_now_time : now += x
    now += get_now[-1]
    return now

dir_making = "사람인공채속보"
try : os.mkdir(dir_making)
except : print("이미 폴더가 생성되어 있습니다.")
max_page = 11

for page_index in range(2, 3) :
    html = urllib.request.urlopen("http://www.saramin.co.kr/zf_user/jobs/public/list/page/%s?sort=ud&listType=public&public_list_flag=y#searchTitle" %str(page_index))
    # xml = html.read().decode("UTF-8")
    # root = ET.fromstring(xml)
    soupData = BeautifulSoup(html, "html.parser")

    title_tag = soupData.findAll('a', attrs = {"str_tit"}) #타이틀 따기
    title_list = []
    for x in title_tag[:title_tag.__len__()] :
        title_list.append(x.text)

    job_sector_tag = soupData.findAll('div', attrs = {"job_sector"})
    job_sector_list = []
    # k = job_sector_tag[0].text[1:] /job_sector 따기
    for x in job_sector_tag[:job_sector_tag.__len__()] :
        job_sector_list.append(x.text[1:])

    recruit_condition_tag = soupData.findAll('td', attrs = {"recruit_condition"}) #학력 따기
    recruit_condition_list = []
    for x in recruit_condition_tag[:recruit_condition_tag.__len__()] :
        temp = ""
        for y in list(x.text[1:]) :
            if y == '\n' : temp += '_'
            else : temp += y
        recruit_condition_list.append(temp)

    company_info_tag = soupData.findAll('td', attrs = {"company_info"}) #회사 정보 따기
    company_info_list = []
    for x in company_info_tag[:company_info_tag.__len__()] :
        temp = ""
        # q = x.text.split('\n')
        for y in x.text.split('\n') :
            if y != '' : temp += y
            else : pass
        company_info_list.append(temp)

    deadlines_tag = soupData.findAll('p', attrs = "deadlines")
    deadlines_list = []
    for x in deadlines_tag :
        deadlines_list.append(x.text)

    result = []
    rrange = int(title_tag.__len__() / 2)

    for x in range(67,68) :
        result.append([title_list[2*x] + title_list[2*x+1]] + [job_sector_list[x]] + [recruit_condition_list[x]] + \
[company_info_list[x]] + [deadlines_list[x]] )
    print("http://www.saramin.co.kr/zf_user/jobs/public/list/page/%s?sort=ud&listType=public&public_list_flag=y#searchTitle" %str(page_index))

    print(result)
    saramin_table = DataFrame(result, columns = ("Job Title", "Job Sector", "Recruit Condition", "Company Info",\
"DeadLines_" + time_change_to_str()))
    saramin_table.to_csv(dir_making + "\\" + "1000대기업 공채속보" + str(page_index) + ".csv", encoding="cp949", mode='w',
index=True)



    # try :
    #     saramin_table.to_csv(dir_making + "\\" + "1000대기업 공채속보" + str(page_index) + ".csv", encoding="cp949", mode='w', index=True)
    # except UnicodeEncodeError as e:
    #     print(e)
    #     print("%s페이지의 정보가 생성 되지 않았습니다." %page_index)



    # for x in range(62,63) :
    #     result.append([title_list[2*x] + title_list[2*x+1]] + [job_sector_list[x]] + [recruit_condition_list[x]] + \
# [company_info_list[x]] + [deadlines_list[x]] )
#     print("http://www.saramin.co.kr/zf_user/jobs/public/list/page/%s?sort=ud&listType=public&public_list_flag=y#searchTitle" %str(page_index))
#
#     saramin_table = DataFrame(result, columns = ("Job Title", "Job Sector", "Recruit Condition", "Company Info",\
# "DeadLines_" + time_change_to_str()))
#     saramin_table.to_csv(dir_making + "\\" + "1000대기업 공채속보" + str(page_index) + ".csv", encoding="cp949", mode='w',
# index=True)


print("End")