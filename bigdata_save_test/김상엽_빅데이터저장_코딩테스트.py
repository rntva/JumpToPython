import json
import pickle

student_ID = "student_ID"
student_name = "student_name"
student_age = "student_age"
student_address = "student_address"
total_class_info = "total_class_info"
num_of_course_learned = "num_of_course_learned"
learning_course_info = "learning_course_info"
course_code = "course_code"
course_name = "course_name"
course_teacher = "course_teacher"
course_open_date = "course_open_date"
course_close_date = "course_close_date"
json_file_name = "ITT_Student.json"
student_index_list_file = "Student_index_list.bin"
g_json_bigdata = []
student_index_list = []

def add_student_info(student_id_input) :
    student_name_input = input("등록하려는 학생의 이름을 입력하십시오.\n(e.g. 김상엽) : ")
    student_age_input = input("등록하려는 학생의 나이를 입력하십시오.\n(e.g. 30) : ")
    student_address_input = input("등록하려는 학생의 주소를 입력하십시오.\n(e.g. 경북 경산시 조영동) : ")
    num_of_course_learned_input = input("등록하려는 학생의 과거 수강 횟수를 입력하십시오.\n(e.g. 0) : ")
    temp_student_info =\
        {
            student_ID : student_id_input, student_name : student_name_input, student_age : student_age_input, student_address : student_address_input,
            total_class_info :
                {
                    num_of_course_learned : num_of_course_learned_input,
                    learning_course_info : []
                }
        }
    g_json_bigdata.append(temp_student_info)
    g_jons_bigdata_index = int(student_id_input[3:])
    add_studnet_total_class_info(g_jons_bigdata_index-1)
    return None

def add_studnet_total_class_info(g_jons_bigdata_index) :
    order_1 = '1'
    while 1 :
        if order_1 == '2' : break
        elif order_1 == '1' :
            course_code_input = input("등록하려는 강의의 코드를 알파벳(2)+숫자(6)로 입력해 주십시오.\n(e.g. IT171106) : ")
            course_name_input = input("해당 강의의 이름을 입력해 주십시오.\n(e.g. IoT 빅데이터 실무반) : ")
            course_teacher_input = input("해당 강의의 강사명을 입력해 주십시오.\n(e.g. 이현구) : ")
            course_open_date_input = input("해당 강의의 개강일을 입력해 주십시오.\n(e.g. 2017-11-06) : ")
            course_close_date_input = input("해당 강의의 종강일을 입력해 주십시오.\n(e.g. 2018-09-05) : ")
            temp_total_class_info =\
                {
                    course_code : course_code_input, course_name : course_name_input, course_teacher : course_teacher_input,
                    course_open_date : course_open_date_input, course_close_date : course_close_date_input
                }
            g_json_bigdata[g_jons_bigdata_index][total_class_info][learning_course_info].append(temp_total_class_info)
        order_1 = input("추가등록을 하시겠습니까?\n(예=1 아니오=2) : ")
    return None

def show_student_info(g_json_bigdata_index) :
    print("\t<학생 정보 출력>")
    print("-학생 ID : %s" %g_json_bigdata[g_json_bigdata_index][student_ID])
    print("-학생 이름 : %s" %g_json_bigdata[g_json_bigdata_index][student_name])
    print("-학생 나이 : %s" %g_json_bigdata[g_json_bigdata_index][student_age])
    print("-학생 주소 : %s" %g_json_bigdata[g_json_bigdata_index][student_address])
    print("-수강 정보( -> ) ")
    print("\t->과거 수강 횟수 : %s" %g_json_bigdata[g_json_bigdata_index][total_class_info][num_of_course_learned])
    if len(g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info]) >= 1 :
        print("\t->현재 수강 과목( => )  ")
        for x in range(len(g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info])) :
            print("\t\t=>강의코드 : %s" %g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info][x][course_code])
            print("\t\t=>강의이름 : %s" %g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info][x][course_name])
            print("\t\t=>강사이름 : %s" %g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info][x][course_teacher])
            print("\t\t=>개강일 : %s" %g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info][x][course_open_date])
            print("\t\t=>종강일 : %s" %g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info][x][course_close_date])
            print()
    else : print("현재 수강중인 과목이 없습니다.")

def show_all() :
    for x in range(len(g_json_bigdata)) :
        show_student_info(x)

def check_condition(stored_data, input_data) :
    divided_stored_data = list(str(stored_data))
    divided_input_data = list(str(input_data))
    starting_index = -1
    append_or_not = -1
    for x in range(len(divided_stored_data)) :
        if divided_stored_data[x] == divided_input_data[0] :
            starting_index = x
            break
    if starting_index != -1 :
        for x in range(len(divided_input_data)) :
            if divided_stored_data[starting_index+x] == divided_input_data[x] : append_or_not = 1
            else :
                append_or_not = -1
                return append_or_not
    return append_or_not

def search_in_first_depth(input_data, category) :
    searched_student_id_list = []
    for x in range(len(g_json_bigdata)) :
        check_condition_result = check_condition(g_json_bigdata[x][category], input_data)
        if check_condition_result == -1 : pass
        elif check_condition_result == 1 :
            searched_student_id_list.append(x)
    if len(searched_student_id_list) == 1 :
        show_student_info(searched_student_id_list[0])
    elif len(searched_student_id_list) >= 2 :
        print("\t<복수 검색 결과가 도출되어 아이디와 이름만 출력합니다.")
        for x in range(len(searched_student_id_list)) :
            print("학생 ID : %s\t학생 이름 : %s" %(g_json_bigdata[x][category], g_json_bigdata[x][category]))
    else : print("검색 결과가 없습니다.")

def search_with_num_of_course_learned(input_data) :
    searched_student_id_list = []
    for x in range(len(g_json_bigdata)):
        check_condition_result = check_condition(g_json_bigdata[x][total_class_info][num_of_course_learned], input_data)
        if check_condition_result == -1:
            pass
        elif check_condition_result == 1:
            searched_student_id_list.append(x)
    if len(searched_student_id_list) == 1:
        show_student_info(searched_student_id_list[0])
    elif len(searched_student_id_list) >= 2:
        print("\t<복수 검색 결과가 도출되어 아이디와 이름만 출력합니다.")
        for x in range(len(searched_student_id_list)):
            print("학생 ID : %s\t학생 이름 : %s" % (g_json_bigdata[x][student_ID], g_json_bigdata[x][student_name]))
    else:
        print("검색 결과가 없습니다.")

def search_in_second_depth(input_data, category) :
    searched_student_id_list = []
    for x in range(len(g_json_bigdata)):
        for y in range(len(g_json_bigdata[x][total_class_info][learning_course_info])) :
            check_condition_result = check_condition(g_json_bigdata[x][total_class_info][learning_course_info][y][category], input_data)
            if check_condition_result == -1:
                pass
            elif check_condition_result == 1:
                searched_student_id_list.append(x)
                break
    if len(searched_student_id_list) == 1:
        show_student_info(searched_student_id_list[0])
    elif len(searched_student_id_list) >= 2:
        print("\t<복수 검색 결과가 도출되어 아이디와 이름만 출력합니다.")
        for x in range(len(searched_student_id_list)):
            print("학생 ID : %s\t학생 이름 : %s" % (g_json_bigdata[x][student_ID], g_json_bigdata[x][student_name]))
    else:
        print("검색 결과가 없습니다.")

def learning_student() :
    searched_student_id_list = []
    for x in range(len(g_json_bigdata)):
        if len(g_json_bigdata[x][total_class_info][learning_course_info]) != 0 :
                searched_student_id_list.append(x)
                break
    if len(searched_student_id_list) == 1:
        show_student_info(searched_student_id_list[0])
    elif len(searched_student_id_list) >= 2:
        print("\t<복수 검색 결과가 도출되어 아이디와 이름만 출력합니다.")
        for x in range(len(searched_student_id_list)):
            print("학생 ID : %s\t학생 이름 : %s" % (g_json_bigdata[x][student_ID], g_json_bigdata[x][student_name]))
    else:
        print("검색 결과가 없습니다.")

def delet_learning_course_info(course_code_input) :
    for x in range(len(g_json_bigdata)):
        for y in range(len(g_json_bigdata[x][total_class_info][learning_course_info])):
            if g_json_bigdata[x][total_class_info][learning_course_info][y][course_code] == course_code_input :
                del g_json_bigdata[x][total_class_info][learning_course_info][y][course_code]
                break

def update_student_info(student_id_input) :
    while 1 :
        g_json_bigdata_index = int(student_id_input[3:])
        print("\t<입력한 ID의 학생 정보는 아래와 같습니다.>")
        print("-학생 ID : %s" %g_json_bigdata[g_json_bigdata_index][student_ID])
        print("-학생 이름 : %s" %g_json_bigdata[g_json_bigdata_index][student_name])
        print("-학생 나이 : %s" %g_json_bigdata[g_json_bigdata_index][student_age])
        print("-학생 주소 : %s" %g_json_bigdata[g_json_bigdata_index][student_address])
        print("-수강 정보( -> ) ")
        print("\t->과거 수강 횟수 : %s" %g_json_bigdata[g_json_bigdata_index][total_class_info][num_of_course_learned])
        if len(g_json_bigdata[g_json_bigdata_index][total_class_info][num_of_course_learned]) >= 1:
            print("\t->현재 수강 과목( => )  ")
            print("\t\t=>강의코드 : ", end='')
            for x in range(len(g_json_bigdata[g_json_bigdata_index][total_class_info][num_of_course_learned])):
                print("%s " %g_json_bigdata[g_json_bigdata_index][total_class_info][learning_course_info][x][course_code], end='')
            print()
        order_1 = input("변경하려는 정보를 선택하여 주십시오.\n\
(학생 이름=1 학생 나이=2 학생 주소=3 과거 수강 횟수=4 현재 수강 과목=5 메인 메뉴=6) : ")
        if order_1 == '6' : break
        elif order_1 == '1' :
            new_student_name = input("변경하려는 이름을 입력하십시오. : ")
            g_json_bigdata[g_json_bigdata][student_name] = new_student_name
        elif order_1 == '2' :
            new_student_age = input("변경하려는 나이를 입력하십시오. : ")
            g_json_bigdata[g_json_bigdata][student_age] = new_student_age
        elif order_1 == '3' :
            new_student_address = input("변경하려는 주소을 입력하십시오. : ")
            g_json_bigdata[g_json_bigdata][student_address] = new_student_address
        elif order_1 == '4' :
            new_num_of_course_learned = input("변경하려는 이름을 입력하십시오. : ")
            g_json_bigdata[g_json_bigdata][total_class_info][num_of_course_learned] = new_num_of_course_learned
        elif order_1 == '5' :
            order_2 = input("변경하려는 과목 코드를 입력하십시오. : ")
            delet_learning_course_info(order_2)
            add_studnet_total_class_info(g_json_bigdata_index)

def delet_student_info() :
    while 1 :
        order_1 = input("학생 ID 삭제=1 강의 코드 삭제=2 메인 메뉴=3\n동작입력 : ")
        if order_1 == '3' : break
        if order_1 == '1' :
            del_student_ID = input("학생 ID를 입력하십시오. : ")
            for x in range(len(g_json_bigdata)):
                if g_json_bigdata[x][student_ID] == del_student_ID  :
                    del g_json_bigdata[x]
                    student_index_list.append("ITT" + "{0:0>3".format(x))
        if order_1 == '2' :
            del_course_code = input("강의 코드를 입력하십시오. : ")
            delet_learning_course_info(del_course_code)

def main_menu() :
    while 1 :
        print("\t\t<학생 정보 관리 시스템입니다.>")
        order_1 = input("동작을 선택해 주십시오.\n\
(학생정보입력=1 학생정보조회=2 학생정보수정=3 학생정보삭제=4 프로그램종료=5)\n동작 입력 : ")
        if order_1 == '5' : break
        elif order_1 == '1' :
            add_student_info(student_index_list.pop())
        elif order_1 == '2' :
            while 1 :
                order_2 = input("\t<학생정보조회>\n\
전체조회=1\n\
아이디로조회=2\n이름으로조회=3\n나이로조회=4\n주소로조회=5\n과거수강횟수로조회=6\n\
수강중인학생으로조회=7\n강의명으로조회=8\n강사명으로조회=9\n메인메뉴로가기=10\n동작입력 : ")
                if order_2 == '10' : break
                elif order_2 == '1' : show_all()
                elif order_2 == '2' :
                    input_data = input("아이디를 입력해 주십시오. : ")
                    search_in_first_depth(input_data, student_ID)
                elif order_2 == '3' :
                    input_data = input("이름을 입력해 주십시오. : ")
                    search_in_first_depth(input_data, student_name)
                elif order_2 == '4' :
                    input_data = input("나이를 입력해 주십시오. : ")
                    search_in_first_depth(input_data, student_age)
                elif order_2 == '5' :
                    input_data = input("주소를 입력해 주십시오. : ")
                    search_in_first_depth(input_data, student_address)
                elif order_2 == '6' :
                    input_data = input("과거 수강 횟수를 해 주십시오. : ")
                    search_with_num_of_course_learned(input_data)
                elif order_2 == '7' :
                    learning_student()
                elif order_2 == '8' :
                    input_data = input("강의명을 입력해 주십시오. : ")
                    search_in_second_depth(input_data, course_name)
                elif order_2 == '9':
                    input_data = input("수강강사를 입력해 주십시오. : ")
                    search_in_second_depth(input_data, course_teacher)
        elif order_1 == '3' :
            input_data = input("학생 아이디를 입력해 주십시오. : ")
            update_student_info(input_data)
        elif order_1 == '4' :
            delet_student_info()

try :
    with open(json_file_name, encoding='UTF8') as json_file :
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_bigdata = json.loads(json_string)
    with open(student_index_list_file, 'rb') as index_file :
        pickle.load(index_file)
        main_menu()
    with open(json_file_name, 'w', encoding='UTF8') as out_file:
            readable_result = json.dumps(g_json_bigdata, indent=4, sort_keys=True, ensure_ascii=False)
            out_file.write(readable_result)
            print("ITT_Student.json SAVED")
    with open(student_index_list_file, 'wb') as index_file:
            pickle.dump(index_file, student_index_list)


except FileNotFoundError :
    order_1 = input("파일이 없습니다.(새로생성=1 경로설정=2) : ")
    if order_1 == '2' :
        path = input("경로를 설정해 주십시오. : ")
        try :
            with open(path + "\\" + json_file_name, encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                g_json_bigdata = json.loads(json_string)
            with open(path + "\\" + student_index_list_file, 'rb') as index_file:
                pickle.load(index_file)
                main_menu()
            with open(path + "\\" + json_file_name, 'w', encoding='UTF8') as out_file:
                readable_result = json.dumps(g_json_bigdata, indent=4, sort_keys=True, ensure_ascii=False)
                out_file.write(readable_result)
                print("ITT_Student.json SAVED")
            with open(path + "\\" + student_index_list_file, 'wb') as index_file:
                pickle.dump(student_index_list, index_file)
        except FileNotFoundError :
            print("파일이 없다. 새로 생성하겠다.")
            order_1 = '1'

    elif order_1 == '1' :
        temp_student_index = ""
        for x in range(1,1000) :
            temp_student_index += "ITT" + "{0:0>3}".format(str(x)) + "\n"
        temp_list = list(reversed(temp_student_index.split('\n')))
        student_index_list = temp_list
        main_menu()
        with open(json_file_name, 'w', encoding='UTF8') as out_file:
            readable_result = json.dumps(g_json_bigdata, indent=4, sort_keys=True, ensure_ascii=False)
            out_file.write(readable_result)
            print("ITT_Student.json SAVED")
        with open(student_index_list_file, 'wb') as index_file :
            pickle.dump(student_index_list, index_file)






