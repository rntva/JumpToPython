try :
    file1 = open("poll.txt", 'r')
    file1.close()
    file1 = open("pool.txt", 'a')
    search_file = ''

except FileNotFoundError :
    token = input("파일을 찾을 수 없습니다. 수행할 작업 번호 선택해 주세요.\n1. 종료\n2. 경로설정\
\n입력 : ")
    if token == '1' :
        print("끝냅니다.")
        search_file = '1'
    elif token == '2' :
        search_file = input("파일 경로를 입력해 주십시오. : ")
        file1 = open(search_file, 'a')

while search_file != "1" :
    survey_answer =  input("프로그래밍이 왜 좋으세요?(종료 입력시 설문 끝) : ")
    if survey_answer == "종료" : break
    survey_answerer_name = input("이름이 어떻게 되십니까? : ")
    file1.write("[%s] %s\n" %(survey_answerer_name, survey_answer))