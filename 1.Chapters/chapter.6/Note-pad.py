import sys

def show_memo(f_object) :
    for x in f_object.readlines():
        print(x, end='')

def add_memo(f_object, str) :
    f_object.write(str)


token = 0

try :
    file1 = open("%s" %sys.argv[1], 'r')
    token = int(input("파일이 존재합니다. 무슨 작업을 원하십니까.\n1.내용보기\n2.내용추가\n  입력 : "))

except FileNotFoundError :
    print("파일이 존재하지 않습니다. 파일을 생성하고 메모를 시작합니다.")
    token = 3
    file1 = open("%s" %sys.argv[1], 'w')

if token == 1 :
    show_memo(file1)
    file1.close()
elif token == 2 :
    file2 = open("%s" %sys.argv[1], 'a')
    add = input("추가할 내용을 입력하세요. : ")
    add_memo(file2, '\n'+add)
    file2.close()
elif token == 3 :
    add = input("추가할 내용을 입력하세요. : ")
    add_memo(file1, add)
    file1.close()