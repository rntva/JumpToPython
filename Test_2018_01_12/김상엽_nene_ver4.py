import urllib.request
import os
import csv
from pandas import DataFrame

def make_nene(data_list, file_index, dir_index) :
    with open(top_dir_name + dir_path + sub_dir_name + dir_index + dir_path + file_name + str(file_index) +\
file_name_extension, 'a') as file :
        temp = csv.writer(file)
        temp.writerow(data_list)

top_dir_name = "V4_BigData"
sub_dir_name = "Nene_data"
dir_path = "\\"
file_name = "nene"
file_name_extension = ".csv"
index_dir_name = "nene_dir_index.txt"
recorded_data_limit = 100
result = []


try :
    with open(top_dir_name + dir_path + file_name + file_name_extension, newline='') as file :
        data = list(csv.reader(file))

except :
    import xml.etree.ElementTree as ET

    response = urllib.request.urlopen(
        'http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s' % (
        urllib.parse.quote('전체'), urllib.parse.quote('전체')))

    xml = response.read().decode('UTF-8')
    root = ET.fromstring(xml)

    for element in root.findall('item'):
        store_name = element.findtext('aname1')
        store_sido = element.findtext('aname2')
        store_gungu = element.findtext('aname3')
        store_address = element.findtext('aname5')
        result.append([store_name] + [store_sido] + [store_gungu] + [store_address])

    nene_table = DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    os.mkdir(top_dir_name)
    nene_table.to_csv(top_dir_name + dir_path + file_name + file_name_extension,\
encoding="cp949", mode='w', index=True)
    with open(top_dir_name + dir_path + file_name + file_name_extension, newline='') as file :
        data = list(csv.reader(file))

top_keys = data[0]
# with open(top_dir_name + dir_path + file_name + '22' + file_name_extension, 'a') as file:
#     print(top_keys)
#     sibal = csv.writer(file)
#     sibal.writerow(top_keys)

try :
    with open(top_dir_name + dir_path + index_dir_name, 'r') as file :
        index = file.readline()
    os.mkdir(top_dir_name + dir_path + sub_dir_name + index)
    count = 1
    for x in range(1, 13):
        with open(top_dir_name + dir_path + sub_dir_name + index + dir_path + file_name + str(x) + \
file_name_extension, 'a') as file:
            temp = csv.writer(file)
            temp.writerow(top_keys)
        for y in data[count:count + 100]:
            make_nene(y, x, index)
        count += 100
    index = str(int(index) + 1)
    with open(top_dir_name + dir_path + index_dir_name, 'w') as file:
        file.write(index)

except :
    os.mkdir(top_dir_name + dir_path + sub_dir_name + '1')
    with open(top_dir_name + dir_path  + index_dir_name, 'w') as file:
        file.write('2')
    count = 1
    for x in range(1, 13) :
        with open(top_dir_name + dir_path + sub_dir_name + '1' + dir_path + file_name + str(x) + \
file_name_extension, 'a') as file:
            temp = csv.writer(file)
            temp.writerow(top_keys)
        for y in data[count:count+100] :
            make_nene(y, x, '1')
        count += 100