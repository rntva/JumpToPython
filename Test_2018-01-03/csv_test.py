import csv
import math


def get_csv_row_instance(primary_key, printing=1):
    try:
        primary_key_index = data[0].index(primary_key)
    except:
        print("No Primary Key Found - Row")
        return None

    get_row_instance = []
    instance_type = ""
    for row in data[1:]:
        if printing == 1: print(row[primary_key_index])
        try:
            get_row_instance.append(float(row[primary_key_index]))
            if instance_type != "str" : instance_type = "float"
        except:
            get_row_instance.append(row[primary_key_index])
            instance_type = "str"
    get_row_instance.append(instance_type)

    return get_row_instance


def get_csv_col_instance(primary_key, printing=1):
    for row in data[1:]:
        if row[0] == primary_key:
            if printing == 1:
                title_name = 0
                for col_instance in row:
                    print("%s : %s" % (data[0][title_name], col_instance), end="   ")
                    title_name += 1
            return row

    print("No Primary Key Found - Col")
    return None


def my_sum(primary_key, printing=1):
    total = 0.0
    try:
        temp_instance = get_csv_row_instance(primary_key, 0)
        if temp_instance[-1] == "str":
            print("str타입은 my_sum작업을 수행하지 않습니다.")
            return None
        elif temp_instance[-1] == "float":
            for x in temp_instance[:-1] :
                total += float(x)
            if printing == 1:
                print("%s : " %primary_key, end = '')
                print(temp_instance)
                print("Sum : %g " %total)
            return total
    except:
        return None

def my_average(primary_key, printing = 1) :
    average = 0.0
    try:
        temp_total = my_sum(primary_key, 0)
        temp_length = len(get_csv_row_instance(primary_key, 0)[:-1])
        if temp_total == None :
            print("total값이 없어 my_average를 수행할 수 없습니다.")
            return None
        else :
            average = temp_total / float(temp_length)
            if printing == 1 : print("%s : total = %g, length = %g, average = %g" %(primary_key,\
temp_total, temp_length, average))
            return average
    except:
        return None

def my_max(primary_key) :
    try :
        if get_csv_row_instance(primary_key, 0)[-1] == "str" :
            print("str타입은 my_min을 수행하지 안습니다.")
            return None

        temp_max = max(get_csv_row_instance(primary_key, 0)[:-1])
        print("%s의 최댓값은 %g" %(primary_key, temp_max))
        return None
    except :None

def my_min(primary_key) :
    try :
        if get_csv_row_instance(primary_key, 0)[-1] == "str" :
            print("str타입은 my_min을 수행하지 안습니다.")
            return None

        temp_min = min(get_csv_row_instance(primary_key, 0)[:-1])
        print("%s의 최댓값은 %g" %(primary_key, temp_min))
        return None
    except : None

def my_deviation(primary_key, printing = 1) :
    temp_deviation = []
    try:
        temp_average = my_average(primary_key, 0)
        if temp_average == None:
            print("average값이 없어 my_deviation를 수행할 수 없습니다.")
            return None
        else:
            for instance in get_csv_row_instance(primary_key, 0)[:-1] :
                if printing == 1 : print("%s %3g - %3g = %g" %(primary_key, instance, temp_average,\
(instance- temp_average)))
                temp_deviation.append(instance - temp_average)
            return temp_deviation
    except:
        return None

def my_variation(primary_key, printing = 1) :
    temp_variation = 0.0
    temp_deviation = my_deviation(primary_key, 0)
    temp_deviation_total = 0.0
    try:
        if temp_deviation == None:
            print("average값이 없어 my_variation를 수행할 수 없습니다.")
            return None
        else:
            for x in temp_deviation:
                temp_deviation_total += float(x)**2
            temp_variation = temp_deviation_total / len(get_csv_row_instance(primary_key, 0)[:-1])
            if printing == 1: print("%s : sum_(deviation^2) = %5g, variation = %g"\
%(primary_key, temp_deviation_total, temp_variation))
            return temp_variation
    except:
        return None

def my_standard_deviation(primary_key) :
    try :
        temp_variation = my_variation(primary_key, 0)
        temp_stan_devi = math.sqrt(temp_variation)
        print("%s : variation = %g, standard deviation = %6g" %(primary_key, temp_variation, temp_stan_devi))
    except : None

def my_ascendant(primary_key, printing = 1) :
    temp = get_csv_row_instance(primary_key, 0)[:-1]
    temp = sorted(temp)
    for x in temp :
        if printing == 1 : print(x)
    return temp

def my_descendant(primary_key) :
    temp = my_ascendant(primary_key, 0)
    temp = reversed(temp)
    for x in temp :
        print(x)
    return temp


with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as file:
    data = list(csv.reader(file))

while 1:
    test_input = input("원하는 동작을 입력하십시오.\n1:get_col 2:get_row 3:sum\
 4:average 5:max 6:min 7:deviation 8:variance 9:standard_deviation\
 10:ascendant 11:decendant 12:exit : ")
    primaty_key = input("primary_key값을 입력하십시오 : ")
    if test_input == '12' : break
    elif test_input == '2' : get_csv_row_instance(primaty_key)
    elif test_input == '1' : get_csv_col_instance(primaty_key)
    elif test_input == '3' : my_sum(primaty_key)
    elif test_input == '4' : my_average(primaty_key)
    elif test_input == '5' : my_max(primaty_key)
    elif test_input == '6' : my_min(primaty_key)
    elif test_input == '7' : my_deviation(primaty_key)
    elif test_input == '8' : my_variation(primaty_key)
    elif test_input == '9' : my_standard_deviation(primaty_key)
    elif test_input == '10' : my_ascendant(primaty_key)
    elif test_input == '11' : my_descendant(primaty_key)