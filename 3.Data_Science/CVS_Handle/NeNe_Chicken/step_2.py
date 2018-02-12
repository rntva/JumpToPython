import csv

def get_csv_row_Instance(row_name) :
    try :
        row_index = data[0].index(row_name)
        row_instance = []
        for row in data[1:]:
            row_instance.append(row[row_index])
        return row_instance
    except ValueError :
        print("찾으려는 Primary_key값이 없습니다.")
        return 1

def get_csv_col_Instance(primary_key) :
    for primary_key_instance in data[1:]:
        if primary_key_instance[0] == primary_key : return primary_key_instance
        else : continue

def print_row(row_instance, type = "int") :
    if row_instance == 1 : return 1
    print("열의 데이터는 아래와 같습니다.")
    if type == "str" :
        for x in row_instance :
            print(x)
        return 0
    elif type == "float" :
        for x in row_instance :
            print(float(x))
        return 0
    elif type == "int" :
        for x in row_instance :
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


with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as file :
    data = list(csv.reader(file))

while 1 :
    access_type = input("Access 데이터 유형을 선택하십시오.(1:행 2:열 3:종료) : ")
    if access_type == '3' : break
    elif access_type == '1' :
        search_primary_key = input("Access하려는 Primary_key를 입력하세요. : ")
        print_col(get_csv_col_Instance(search_primary_key))
    elif access_type == '2' :
        search_row_info = input("찾고싶은 Primary_key와 출력타입(기본은 int형)을 입력하십시오.(, )로 구분\
\ne.g)PERCENT FEMALE, float <-- PERCENT FEMALE을 float타입으로 출력\
\ne.g)PERCENT FEMALE, str   <-- PERCENT FEMALE을 string타입으로 출력\
\ne.g)COUNT FEMALE         <-- COUNT FEMALE을 Int타입으로 출력\n입력해주세요 : ").split(', ')
        print_type = ""
        try :
            print_type = search_row_info[1]
        except :
            print_type = "int"
        row_instance = get_csv_row_Instance(search_row_info[0])
        print_row(row_instance, print_type)