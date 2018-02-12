import csv

def get_csv_row_Instance(row_name) :
    count_row_name_index = data[0].index(row_name)
    count_Participants = []
    for row in data[1:]:
        count_Participants.append(int(row[count_row_name_index]))
    return  count_Participants

with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as file :
    data = list(csv.reader(file))

count_Participants_Index = data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS' : " + str(count_Participants_Index))
count_Participants = []
for row in data[1:] :
    count_Participants.append(int(row[count_Participants_Index]))
for x in count_Participants : print(x, end = ' ')
print()

count_Citizen_Status_Total_Index = data[0].index("COUNT CITIZEN STATUS TOTAL")
print("The index of 'COUNT CITIZEN STATUS TOTAL' : " + str(count_Citizen_Status_Total_Index))
count_Citizen_Status_Total = []
for row in data[1:] :
    count_Citizen_Status_Total.append(int(row[count_Citizen_Status_Total_Index]))
for x in count_Citizen_Status_Total : print(x, end = ' ')
print()

search_row_info = input("찾고싶은 정보를 입력하십시오. : ")
# count_search_row_index = data[0].index(search_row_info)
# count_Participants = []
# for row in data[1:] :
#     count_Participants.append(int(row[count_Participants_Index]))
print(get_csv_row_Instance(search_row_info))




# COUNT_CITIZEN_STATUS_TOTAL = []
# for row in data[1:] :
#     count_Participants_Index.append(int(row[count_Participants_Index]))

# count = 0
# for row in data[0] :
#     if row == "COUNT CITIZEN STATUS TOTAL" :
#         print(count)
#         break
#     else : count += 1
