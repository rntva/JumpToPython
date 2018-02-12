# try :
#     file1 = open("poll.txt", 'r')
# except FileNotFoundError :
#     file1 = open("poll.txt", 'a')
#     file1.write('\n')

file1 = open("poll.txt", 'a')

while 1 :
    survey_answer =  input("프로그래밍이 왜 좋으세요?(종료 입력시 설문 끝) : ")
    if survey_answer == "종료" : break
    survey_answerer_name = input("이름이 어떻게 되십니까? : ")
    file1.write("[%s] %s\n" %(survey_answerer_name, survey_answer))
