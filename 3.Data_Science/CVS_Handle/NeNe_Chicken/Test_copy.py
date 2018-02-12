import csv
import math

def get_row_data(primary_key, printing = 1) :
    primary_key_index = data[0].index(primary_key)
    primary_key_list = []
    for row in data[1:] :
        if printing == 1 : print(row[primary_key_index])
        primary_key_list.append(row[primary_key_index])

    return primary_key_list

with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as file :
    data = list(csv.reader(file))

primary_key = input("출력하려는 row의 primary_ksy값을 입력하십시오. : ")
print(get_row_data(primary_key, 0))
#