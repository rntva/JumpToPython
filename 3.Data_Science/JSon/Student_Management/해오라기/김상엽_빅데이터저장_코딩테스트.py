import json
import pickle

student_ID = "student_ID"
student_name = "student_name"
student_age = "student_age"
student_address = "student_address"
total_course_info = "total_course_info"
num_of_course_learned = "num_of_course_learned"
total_course_info = "total_course_info"
learning_course_info = "learning_course_info"
course_code = "course_code"
course_name = "course_name"
course_teacher = "course_teacher"
course_open_date = "course_open_date"
course_close_date = "course_close_date"

json_file_name = "ITT_Student.json"
g_json_bigdata_id_index_file = "ITT_Student_ID_Index.txt"
g_json_bigdata_left_id_list = []
g_json_bigdata = []
student_index_list = []
# temp_total_course_info = []

def add_student_total_course_info(student_index) :
    while 1 :
        order_1 = input("현재 수강 과목 정보를 추가하시겠습니까?(예=1 아니오=1)\n\
입력동작 : ")
        if order_1 == '2':
            break
        elif order_1 == '1':
            course_code_input = input("학생이 수강중인 강의코드를 입력하십시오.(강의코드 알파벳 2자리 + 개걍 년,월,일 6자리)\n\
    (e.g. IB171106) : ")
            course_name_input = input("해당 강의코드의 강의명을 입력하십시오.\n\
    (e.g. IoT 빅데이터 실무반) : ")
            course_teacher_input = input("해당 강의코드의 강사명을 입력하십시오.\n\
    (e.g. 이현구) : ")
            course_open_date_input = input("해당 강의코드의 개강날짜를 입력하십시오.\n\
    (e.g. 2017-11-06) : ")
            course_close_date_input = input("해당 강의코드의 종강날짜를 입력하십시오.\n\
    (e.g. 2018-09-05) : ")
            g_json_bigdata[0][student_index][total_course_info][learning_course_info][0][course_code_input] = \
                {
                    course_name: course_name_input, course_teacher: course_teacher_input,
                    course_open_date: course_open_date_input, course_close_date: course_close_date_input
                }
    return None

def add_student_info(student_index) :
    student_name_input = input("학생 이름을 입력해 주십시오.\n\
(e.g. 김상엽) : ")
    student_age_input = input("학생 나이를 입력해 주십시오.\n\
(e.g. 30) : ")
    student_address_input = input("학생 주소를 입력해 주십시오.\n\
(e.g.  경북 경산시 조영동) : ")
    num_of_course_learned_input = input("과거 수강 횟수를 입력해 주십시오.\n\
(e.g. 0) : ")
    g_json_bigdata[0][student_index] =\
        {
            student_name : student_name_input,
            student_age : student_age_input,
            student_address :student_address_input,
            total_course_info :
                {
                    num_of_course_learned : num_of_course_learned_input,
                    learning_course_info : {}
                }
        }
    add_student_total_course_info(student_index)
    return None

def show_student_info(student_index) :
    print("<학생정보>")
    print("-학생아이디 : %s" %student_index)
    print("-학생이름 : %s" %g_json_bigdata[0][student_index][student_name])
    print("-학생나이 : %s" %g_json_bigdata[0][student_index][student_age])
    print("-학생주소 : %s" %g_json_bigdata[0][student_index][student_address])
    print("-수강정보")
    print("--과거수강횟수 : %s" %g_json_bigdata[0][student_index][total_course_info][num_of_course_learned])
    temp_attending_class_keys_list = list(g_json_bigdata[0][student_index][total_course_info][learning_course_info][0].keys())
    for y in temp_attending_class_keys_list:
        print("--현재수강과목코드 : %s" % y)
        print("--현재수강강의이름 : %s" %g_json_bigdata[0][student_index][total_course_info][learning_course_info][0][y][course_name])
        print("--현재수강강의교사 : %s" %g_json_bigdata[0][student_index][total_course_info][learning_course_info][0][y][course_teacher])
        print("--현재수강강의개강 : %s" %g_json_bigdata[0][student_index][total_course_info][learning_course_info][0][y][course_open_date])
        print("--현재수강강의종강 : %s" %g_json_bigdata[0][student_index][total_course_info][learning_course_info][0][y][course_close_date])
        print()
    return None

def get_student_index_list() :
    global student_index_list
    student_index_list = list(g_json_bigdata[0].keys())
    return None

def show_all() :
    for x in student_index_list :
        print(show_student_info(x))
        print("------------------------------------------------------------------------")
    return None

def check_codition(stored_data, input_data) :
    divide_stored_data = list(str(stored_data))
    divide_inputted_data = list(str(input_data))
    append_or_not = '0'
    starting_index = -1
    for x in range(len(divide_stored_data)) :
        if divide_stored_data[x] == divide_inputted_data[0] :
            starting_index = x
            break
    if starting_index == -1 : return append_or_not
    elif starting_index != -1 :
        for x in range(len(divide_inputted_data)) :
            try :
                if divide_stored_data[starting_index+x] == divide_inputted_data[x] : append_or_not = '1'
                else :
                    append_or_not = '0'
                    return append_or_not
            except :
                append_or_not = '0'
                return append_or_not
        return append_or_not

def show_searched_student_info(searched_student_name_list) :
    if len(searched_student_name_list) == 1:
        show_student_info(searched_student_name_list[0])
    elif len(searched_student_name_list) > 1:
        print("2개 이상의 결과가 검색되어 아이디와 이름만 보여줍니다.")
        for x in searched_student_name_list:
            print("아이디 : %s    이름 : %s " %(x, g_json_bigdata[0][x][student_name]))
    elif searched_student_name_list == []:
        print("수강중인 학생이 없습니다.")
    return None

def search_with_student_primary_key(input_data) :
    searched_student_name_list = []
    for x in student_index_list :
        if check_codition(x, input_data) == '1' :
            searched_student_name_list.append(x)
    show_searched_student_info(searched_student_name_list)
    return None

def search_into_one_depth(input_data_category, input_data) :
    searched_student_name_list = []
    for x in student_index_list:
        if check_codition(g_json_bigdata[0][x][input_data_category], input_data) == '1':
            searched_student_name_list.append(x)
    show_searched_student_info(searched_student_name_list)
    return None

def search_with_past_registrarion(student_ragistrantion) :
    searched_student_name_list = []
    for x in student_index_list :
        if check_codition(g_json_bigdata[0][x][total_course_info][num_of_course_learned], student_ragistrantion) == '1' :
            searched_student_name_list.append(x)
    show_searched_student_info(searched_student_name_list)
    return None

def search_with_now_studying() :
    searched_student_name_list = []
    for x in student_index_list :
        if list(g_json_bigdata[0][x][total_course_info][learning_course_info].keys()) != [] :
            searched_student_name_list.append(x)
    show_searched_student_info(searched_student_name_list)
    return None

def search_into_two_depth(input_data_category, input_data) :
    searched_student_name_list = []
    for x in student_index_list:
        student_class_code_list = list(g_json_bigdata[0][x][total_course_info][learning_course_info].keys())
        for y in student_class_code_list:
            if check_codition(g_json_bigdata[0][x][total_course_info][learning_course_info][y][input_data_category], input_data) == '1':
                searched_student_name_list.append(x)
                break
    show_searched_student_info(searched_student_name_list)
    return None

def delet_with_student_primary_key(student_index) :
    for x in student_index_list :
        if student_index == x :
            del(g_json_bigdata[0][x])
            g_json_bigdata_left_id_list.append(student_index)
            return None

def update_student_info(primary_key) :
    for x in student_index_list :
        if primary_key == x[1] :
            while 1 :
                print("선택하신 아이디의 정보는 아래와 같습니다.")
                print("1:학생이름 : %s" % g_json_bigdata[0][x][student_name])
                print("2:학생나이 : %s" % g_json_bigdata[0][x][student_age])
                print("3:학생주소 : %s" % g_json_bigdata[0][x][student_address])
                print("-수강정보")
                print("4:과거수강횟수 : %s" % g_json_bigdata[0][x][total_course_info][num_of_course_learned])
                temp_attending_class_keys_list = list(g_json_bigdata[0][x][total_course_info][num_of_course_learned].keys())
                print("5:현재수강강의 코드 : ", end = '')
                print(temp_attending_class_keys_list)
                print("6:현재수강강의 추가 : ")
                print("7:수정 끝")
                order_1 = input("바꾸려는 정보를 선택하십시오. : ")
                if order_1 == '7' : break
                elif order_1 == '1' :
                    new_name = input("이름을 입력하십시오.\ne.g)김상엽 : ")
                    g_json_bigdata[0][x][student_name] = new_name
                elif order_1 == '2' :
                    new_age = input("나이를 입력하십시오.\ne.g)30 : ")
                    g_json_bigdata[0][x][student_age] = new_age
                elif order_1 == '3' :
                    new_address = input("주소를 입력하십시오.\ne.g)경북 경산시 조영동 : ")
                    g_json_bigdata[0][x][student_address] = new_address
                elif order_1 == '4' :
                    new_p_registration = input("과거수강횟수를 입력하십시오.\ne.g)0 : ")
                    g_json_bigdata[0][x][total_course_info][num_of_course_learned] = new_p_registration
                elif order_1 == '5' :
                    c_code_from = input("바꾸려는 강의를 코드를 입력하십시오. : ")
                    print(">>현재수강강의이름 : %s" %g_json_bigdata[0][x][total_course_info][num_of_course_learned][c_code_from][course_name])
                    print(">>현재수강강의교사 : %s" %g_json_bigdata[0][x][total_course_info][num_of_course_learned][c_code_from][course_teacher])
                    print(">>현재수강강의개강 : %s" %g_json_bigdata[0][x][total_course_info][num_of_course_learned][c_code_from][course_open_date])
                    print(">>현재수강강의종강 : %s" %g_json_bigdata[0][x][total_course_info][num_of_course_learned][c_code_from][course_close_date])
                    order_2 = input("현재 수강 과목 정보를 수정하시겠습니까?(1:예 2:아니오 3:삭제) : ")
                    if order_2 == '2' : pass
                    elif order_2 == '1' :
                        print()
                        del(g_json_bigdata[0][x][total_course_info][num_of_course_learned][c_code_from])
                        add_student_total_course_info(primary_key)
                    elif order_2 == '3' : del(g_json_bigdata[0][x][total_course_info][num_of_course_learned][c_code_from])
                elif order_1 == '6' :
                    print()
                    add_student_total_course_info(primary_key)
    return None

def main_function() :
    global student_index_list
    print("학생 정보 관리 프로그램입니다.".center(30))
    while 1 :
        order_1 = input("\n동작을 선택해 주십시오.\n\
1:학생 정보입력\n2:학생 정보조회\n3:학생 정보수정\n4:학생 정보삭제\n5:프로그램 종료\n동작입력 : ")
        if order_1 == '5' : break
        elif order_1 == '1' :
            print()
            while 1 :
                print()
                g_json_bigdata.append(add_student_info(student_index_list.pop()))
                student_index_list = get_student_index_list()
                order_2 = input("계속 하시겠습니까?(1:예 2:아니오) : ")
                if order_2 == '2' : break
                elif order_2 == '1' : continue
        elif order_1 == '2' :
            print()
            while 1 :
                order_2 = input("\n1:전체정보출력\n2:ID로조회\n3:이름으로조회\n4:나이로조회\n5:주소로조회\n6:과거수강횟수로조회\n\
7:현재강의를수강하는학생으로조회\n8:현재수강과목의강의명으로조회\n9:현재수강과목의강사로조회\n10:상위메뉴로\n동작입력 : ")
                if order_2 == '10' : break
                elif order_2 == '1' :
                    print()
                    show_all()
                elif order_2 == '2' :
                    print()
                    input_data = input("아이디를 입력하세요. : ")
                    search_with_student_primary_key(input_data)
                elif order_2 == '3' :
                    print()
                    input_data = input("이름을 입력하세요. : ")
                    search_into_one_depth(student_name, input_data)
                elif order_2 == '4' :
                    print()
                    input_data = input("나이를 입력하세요. : ")
                    search_into_one_depth(student_age, input_data)
                elif order_2 == '5' :
                    print()
                    input_data = input("주소를 입력하세요. : ")
                    search_into_one_depth(student_address, input_data)
                elif order_2 == '6' :
                    print()
                    input_data = input("과거수강횟수를 입력하세요. : ")
                    search_with_past_registrarion(input_data)
                elif order_2 == '7' :
                    print()
                    search_with_now_studying()
                elif order_2 == '8' :
                    print()
                    input_data = input("현재수강과목의강의명을 입력하세요. : ")
                    search_into_two_depth(course_name, input_data)
                elif order_2 == '9' :
                    print()
                    input_data = input("현재수강과목의강사명을 입력하세요. : ")
                    search_into_two_depth(course_teacher, input_data)
        elif order_1 == '3' :
            print()
            input_data = input("수정하려는 아이디를 입력하십시오. : ")
            update_student_info(input_data)
            student_index_list = get_student_index_list()
        elif order_1 == '4' :
            print()
            input_data = input("삭제하려는 아이디를 입력하십시오. : ")
            delet_with_student_primary_key(input_data)
            student_index_list = get_student_index_list()
    return None

while 1 :
    try :
        with open(json_file_name, encoding='UTF8') as json_file :
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            g_json_bigdata = json.loads(json_string)
        with open(g_json_bigdata_id_index_file, 'rb') as json_index:
            student_index_list = pickle.load(json_index)
        main_function()
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            jsonResult = g_json_bigdata
            readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
        with open(g_json_bigdata_id_index_file, 'wb') as json_index:
            pickle.dump(student_index_list, json_index)
        break

    except FileNotFoundError :
        file_not_found = input("%s파일을 찾을 수 없습니다. 다음 동작을 선택해 주십시오.\n1:신규생성 2:경로설정" %json_file_name)
        if file_not_found == '2' :
            path = input("경로를 입력해 주십시오.\ne.g)D:\\Pycharm_projects\\Emigration\\Jason_Practice\\ : ")
            try:
                with open(path + json_file_name, encoding='UTF8') as json_file:
                    json_object = json.load(json_file)
                    json_string = json.dumps(json_object)
                    g_json_big_data = json.loads(json_string)
                with open(path + g_json_bigdata_id_index_file, 'rb') as index_file:
                    left_primary_key_index_list = pickle.load(index_file)
                student_primary_key_list = get_student_index_list()
                main_function()
                with open(path + json_file_name, 'w', encoding='utf8') as outfile:
                    jsonResult = g_json_big_data
                    readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                with open(path + g_json_bigdata_id_index_file, 'wb') as json_index:
                    pickle.dump(left_primary_key_index_list, json_index)
                break
            except:
                print("해당 경로에도 파일이 없습니다. 기본 경로에서 신규생성을 합니다.")
                file_not_found = '1'
        if file_not_found == '1' :
            temp_id_index_str = ""
            for x in range(1,1000) :
                temp_id_index_str += "ITT" + "{0:0>3}".format(str(x)) + '\n'
            temp_id_index_list = list(reversed(temp_id_index_str[:-1].split('\n')))
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                json_big_dict = []
                while 1:
                    order_1 = input("학생정보를 추가하시겠습니까?(1:예 2:아니오) : ")
                    if order_1 == '2':
                        break
                    elif order_1 == '1':
                        g_json_bigdata.append(add_student_info(temp_id_index_list.pop()))
                jsonResult = g_json_bigdata
                readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')
            with open(g_json_bigdata_id_index_file, 'wb') as index_file:
                pickle.dump(student_index_list, index_file)
                print("%s파일 생성 완료" %g_json_bigdata_id_index_file)
        else : print("동작 선택 좀 똑디 하소.")

