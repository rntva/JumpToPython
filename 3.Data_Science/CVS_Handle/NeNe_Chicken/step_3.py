import csv
import math

def get_csv_row_Instance(row_name) :
    type = ""
    try :
        row_index = data[0].index(row_name)
        row_instance = []
        for row in data[1:]:
            row_instance.append(row[row_index])
            if row[row_index] != 0 and type != "float" and type != "str" :
                try :
                    type = row[row_index].split('.')[1]
                    type = "float"
                except :
                    try :
                        int(row[row_index])
                        type = "int"
                    except :
                        type = "str"
        row_instance.append(type)
        return row_instance
    except ValueError :
        print("찾으려는 Primary_key값이 없습니다.")
        return 1

def get_csv_col_Instance(primary_key) :
    for primary_key_instance in data[1:]:
        if primary_key_instance[0] == primary_key : return primary_key_instance
        else : continue

def print_row(row_instance) :
    if row_instance == 1 : return 1
    print("열의 데이터는 아래와 같습니다.")
    if row_instance[-1] == "str" :
        for x in row_instance :
            print(x)
        return 0
    elif row_instance[-1] == "float" :
        for x in row_instance[:-1] :
            print(float(x))
        return 0
    elif row_instance[-1] == "int" :
        for x in row_instance[:-1] :
            print(int(x))
        return 0
    else :
        print("출력타입 설정이 잘 못 되었습니다.")
        return 1

def print_col(primary_key_instance) :
    counting = 0
    print("행의 데이터는 아래와 같습니다.")
    try :
        for x in primary_key_instance :
            print("%s : %-10s" %(data[0][counting], x), end ='' )
        print()
        return 0
    except TypeError :
        print("찾는 Primaty_key가 없습니다.")
        return 1

def my_sum(row_name, printing = 1) :
    sum = 0
    row_instance = get_csv_row_Instance(row_name)
    if row_instance[-1] == "str" : return "문자열입니다."
    else :
        if row_instance[-1] == "float" :
            for x in row_instance[:-1]:
                if printing == 1 : print(x, end = ' ')
                sum += float(x)
            if printing == 1 : print()
            return sum
        elif row_instance[-1] == "int" :
            for x in row_instance[:-1]:
                if printing == 1 : print(x, end = ' ')
                sum += int(x)
            if printing == 1 : print()
            return sum

def my_average(row_name) :
    return my_sum(row_name, 0) / len(get_csv_row_Instance(row_name)[:-1])

def my_max(row_name) :
    row_instance = get_csv_row_Instance(row_name)
    my_sum(row_name)
    if row_instance[-1] == "str" : return "문자열입니다."
    else :
        if row_instance[-1] == "float" :
            return max(list(map(float, row_instance[:-1])))
        elif row_instance[-1] == "int" :
            return max(list(map(int, row_instance[:-1])))

def my_min(row_name) :
    row_instance = get_csv_row_Instance(row_name)
    my_sum(row_name)
    if row_instance[-1] == "str" : return "문자열입니다."
    else :
        if row_instance[-1] == "float" :
            return min(list(map(float, row_instance[:-1])))
        elif row_instance[-1] == "int" :
            return min(list(map(int, row_instance[:-1])))

def my_deviation(row_name, printing = 1) :
    row_instance = get_csv_row_Instance(row_name)
    row_average = my_average(row_name)
    row_divations = []
    if row_instance[-1] == "str" : return "문자열입니다."
    else :
        for x in row_instance[:-1]:
            if printing == 1 : print("%0.4f = %g + %0.4f" %((float(x) - row_average), float(x), row_average))
            row_divations.append(float(x) - float(row_average))
    return row_divations

def my_variance(row_name) :
    row_variance = 0.0
    temp = my_deviation(row_name, 0)[:-1]
    for x in temp :
        row_variance += (x - my_average(row_name))**2 / len(get_csv_row_Instance(row_name)[:-1])
    return row_variance

def my_standard_deviation(row_name) :
    return math.sqrt(my_variance(row_name))

def my_ascendant(row_name, printing = 1) :
    row_instance = get_csv_row_Instance(row_name)
    if row_instance[-1] == "str":
        return "문자열입니다."
    else:
        if row_instance[-1] == "float":
            temp = sorted(list(map(float, row_instance[:-1])))
        elif row_instance[-1] == "int":
            temp = sorted(list(map(int, row_instance[:-1])))
    if printing == 1 :
        for x in temp : print(x)
    return temp

def my_descendant(row_name) :
    temp = reversed(my_ascendant(row_name, 0))
    for x in temp : print(x)
    return temp

with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as file :
    data = list(csv.reader(file))

while 1 :
    access_type = input("Access 데이터 유형을 선택하십시오.\n\
(1:행 2:열 3:총합 4:평균 5:최댓값 6:최솟값 7:편차 8:분산 9:표준편차 10:오름차순 11:내림차순 12:종료) : ")
    if access_type == '12' : break
    elif access_type == '1' :
        search_primary_key = input("Access하려는 Primary_key를 입력하세요. : ")
        print_col(get_csv_col_Instance(search_primary_key))
    elif access_type == '2' :
        search_row_info = input("Access하려는 Primary_key를 입력하십시오. : ")
        print_row(get_csv_row_Instance(search_row_info))
    elif access_type == '3' :
        search_row_info = input("총합을 구하려는 Primary_key를 입력하십시오. : ")
        print("값이 위와 같으니 SUM = " + str(my_sum(search_row_info)))
    elif access_type == '4':
        search_row_info = input("평균을 구하려는 Primary_key를 입력하십시오. : ")
        print("값이 위와 같으니 SUM = " + str(my_sum(search_row_info)) + " AVERAGE = "\
+ str(my_average(search_row_info)))
    elif access_type == '5':
        search_row_info = input("최댓값을 구하려는 Primary_key를 입력하십시오. : ")
        print("값이 위와 같으니 MAX = " + str(my_max(search_row_info)))
    elif access_type == '6':
        search_row_info = input("최솟값을 구하려는 Primary_key를 입력하십시오. : ")
        print("값이 위와 같으니 MIN = " + str(my_min(search_row_info)))
    elif access_type == '7':
        search_row_info = input("편차를 구하려는 Primary_key를 입력하십시오. : ")
        my_sum(search_row_info)
        my_deviation(search_row_info)
    elif access_type == '8':
        search_row_info = input("분산을 구하려는 Primary_key를 입력하십시오. : ")
        print("분산(Variance) 공식: ∑(표본-평균)**/표본수")
        print(my_variance(search_row_info))
    elif access_type == '9':
        search_row_info = input("표준편자를 구하려는 Primary_key를 입력하십시오. : ")
        print("표준편차(Standard Deviation) 공식: √분산")
        print(my_standard_deviation(search_row_info))
    elif access_type == '10':
        search_row_info = input("오름차순으로 출력하려는 Primary_key를 입력하십시오. : ")
        my_ascendant(search_row_info)
    elif access_type == '11':
        search_row_info = input("내림차순으로 출력하려는 Primary_key를 입력하십시오. : ")
        my_descendant(search_row_info)

        #         search_row_info = input("찾고싶은 Primary_key와 출력타입(기본은 int형)을 입력하십시오.(, )로 구분\
        # \ne.g)PERCENT FEMALE, float <-- PERCENT FEMALE을 float타입으로 출력\
        # \ne.g)PERCENT FEMALE, str   <-- PERCENT FEMALE을 string타입으로 출력\
        # \ne.g)COUNT FEMALE         <-- COUNT FEMALE을 Int타입으로 출력\n입력해주세요 : ").split(', ')
        #         print_type = ""
        #         try :
        #             print_type = search_row_info[1]
        #         except :
        #             print_type = "int"
        #         row_instance = get_csv_row_Instance(search_row_info[0])
        #         print_row(row_instance, print_type)
# print("값이 위와 같으니 SUM = " + str(my_sum("COUNT FEMALE")))
# print("값이 위와 같으니 AVERAGE = " + str(my_average("COUNT FEMALE")))
# print("값이 위와 같으니 MAX = " + str(my_max("COUNT FEMALE")))
# print("값이 위와 같으니 MIN = " + str(my_min("COUNT FEMALE")))
# print("값이 위와 같으니 SUM = " + str(my_sum("PERCENT FEMALE")))
# print("값이 위와 같으니 AVERAGE = " + str(my_average("PERCENT FEMALE")))
# print("값이 위와 같으니 MAX = " + str(my_max("PERCENT FEMALE")))
# print("값이 위와 같으니 MIN = " + str(my_min("PERCENT FEMALE")))
# my_deviation("COUNT FEMALE")
# my_deviation("PERCENT FEMALE")

# print(my_variance("COUNT FEMALE"))
# print(my_standard_deviation("COUNT FEMALE"))
# my_ascendant("COUNT FEMALE")
# my_descendant("COUNT FEMALE")
# my_variance("PERCENT FEMALE")
