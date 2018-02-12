#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
import csv
from pandas import DataFrame
import xml.etree.ElementTree as ET

def make_dir(index) :
    try:
        os.mkdir(dir_name + dir_path + nene_dir + index)
        return index
    except:
        index = int(index)
        index += 1
        index = str(index)
        make_dir(index)
        return index

def make_nene(dir_index, file_index, data_line) :
    with open(dir_name + dir_path + nene_dir + dir_index + dir_path + nene_file + file_index + e_csv ,\
'a', newline='') as file1 :
       temp = csv.writer(file1)
       temp.writerow(data_line)
    return None


result = []
nene_file = "nene"
nene_dir = "Nene_Data"
e_csv = ".csv"
dir_name = "V4_BigData"
dir_path = "\\"
record_limit = 100
file_limiet = 12

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))
nene_table.to_csv('nene.csv',encoding="cp949",mode='w',index=True)


try : os.mkdir(dir_name)
except : pass

with open("nene.csv", newline='') as file :
    data = list(csv.reader(file))
top_table = data[0]

counting_data = 0
counting_file = 1
counting_dir = 1

if counting_data == 0 and counting_file == 1 and counting_dir == 1:
    counting_dir = make_dir(str(counting_dir))
    for data_ilne in data[:101]:
        make_nene(str(counting_dir), str(counting_file), data_ilne)
        counting_data += 1

while 1 :
    if (counting_data - 1) % 100 == 0:
        counting_file += 1
        make_nene(str(counting_dir), str(counting_file), top_table)
    if len(data) <= counting_data : break
    elif counting_data >= 2:
        make_nene(str(counting_dir), str(counting_file), data[counting_data])
        counting_data += 1
print("End")