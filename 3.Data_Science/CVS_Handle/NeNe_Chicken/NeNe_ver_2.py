#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET

def make_dir(index) :
    os.mkdir(dir_name + dir_path + nene_dir+index)
    return None

def make_nene(dir_index, file_index) :
    nene_table.to_csv(dir_name + dir_path + nene_dir + dir_index + "\\" + nene_file + file_index + csv,\
encoding="cp949", mode='w', index=True)
    return None

result = []
nene_file = "nene"
nene_dir = "Nene_Data"
csv = ".csv"
record_limit = 3
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
dir_name = "V2_BigData"
dir_path = "\\"
try : os.mkdir(dir_name)
except : pass
try :
    with open(dir_name + dir_path + "nene_index.txt", 'r') as file :
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index / record_limit)
        if file_index % record_limit != 0 : dir_index = str(dir_index+1)
        else : dir_index = str(dir_index)
        if file_index % record_limit == 1 and file_index >= (record_limit+1) :
            dir_index = str(dir_index)
            make_dir(dir_index)
        else : None
        file_index = str(file_index)
        make_nene(dir_index, file_index)
        file_index = int(file_index)
        file_index += 1
        file_index = str(file_index)
    with open(dir_name + dir_path + "nene_index.txt", 'w') as file :
        file.write(file_index)
except FileNotFoundError :
    with open(dir_name + dir_path + "nene_index.txt", 'w') as file :
        file.write('2')
    make_dir('1')
    make_nene('1', '1')
print("End")