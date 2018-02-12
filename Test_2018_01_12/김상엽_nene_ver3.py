import urllib.request
import os
import time
from pandas import DataFrame

def time_change_to_str() :
    now = ""
    get_now = time.ctime().split(' ')
    get_now_time = get_now[3].split(':')
    for x in get_now[:3] : now += x
    for x in get_now_time : now += x
    now += get_now[-1]
    return now

top_dir_name = "V3_BigData"
sub_dir_name = "Nene_data"
dir_path = "\\"
file_name = "nene"
file_name_extension = ".csv"
index_file_name = "nene_csv_index.txt"
record_limit = 3
result = []

import xml.etree.ElementTree as ET
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))

try :
    with open(top_dir_name + dir_path + index_file_name, 'r') as file :
        index = file.readline()
    if int(index) % record_limit == 1 and int(index) != 2 :
        temp = int(int(index) / record_limit) + 1
        os.mkdir(top_dir_name + dir_path + sub_dir_name + str(temp))
    elif int(index) % record_limit == 0 : temp = int(int(index) / record_limit)
    else : temp = int(int(index) / record_limit) + 1
    nene_table.to_csv(top_dir_name + dir_path + sub_dir_name + str(temp) + dir_path +\
file_name + time_change_to_str() + file_name_extension, encoding="cp949",mode='w',index=True)
    index = int(index)
    index += 1
    index = str(index)
    with open(top_dir_name+dir_path+index_file_name, 'w') as file:
        file.write(index)
except :
    os.mkdir(top_dir_name)
    os.mkdir(top_dir_name + dir_path + sub_dir_name + '1')
    with open(top_dir_name + dir_path  + index_file_name, 'w') as file:
        file.write('2')
    nene_table.to_csv(top_dir_name + dir_path + sub_dir_name + '1' + dir_path + file_name +\
time_change_to_str() + file_name_extension, encoding="cp949", mode='w', index=True)