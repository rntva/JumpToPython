import sys

def a_style(argv_1, argv_2, up = False) :
    if up == True :
        file_1 = open(argv_1, 'a')
        argv_2 = str(argv_2).upper()
        file_1.write(argv_2)
        file_1.close()
    else :
        file_1 = open(argv_1, 'a')
        file_1.write(argv_2)
        file_1.close()

def v_style(file_1) :
    for x in file_1.readlines() :
        print(x)

if sys.argv[1] == '-a' :
    try :
        file_1 = open("memo.txt", 'r')
        file_1.close()
        a_style("memo.txt", sys.argv[2])
    except FileNotFoundError :
        order = input("아래 중 선택하세요.\n1. 새로 생성하시겠습니까?\n2. 파일 경로를 입력하겠습니다.")
        if order == '1' : a_style("memo.txt", sys.argv[2])
        elif order == '2' :
            file_pass = input("경로를 입력하세요. : ")
            a_style(file_pass+"\\memo.txt", sys.argv[2])
elif sys.argv[1] == '-au' :
    try :
        file_1 = open(sys.argv[1], 'r')
        file_1.close()
        a_style("memo.txt", sys.argv[2], True)
    except FileNotFoundError :
        order = input("아래 중 선택하세요.\n1. 새로 생성하시겠습니까?\n2. 파일 경로를 입력하겠습니다.")
        if order == '1' : a_style("memo.txt", sys.argv[2], True)
        elif order == '2' :
            file_pass = input("경로를 입력하세요. : ")
            a_style(file_pass+"\\memo.txt", sys.argv[2], True)
elif sys.argv[1] == '-v' :
    try :
        file_1 = open("memo.txt", 'r')
        v_style(file_1)
    except :
        order = input("아래 중 선택하세요.\n1. 종료하시겠습니까?\n2. 파일 경로를 입력하겠습니다.")
        if order == '2':
            file_pass = input("경로를 입력하세요. : ")
            file_1 = open(file_pass+"\\memo.txt", 'r')
            v_style(file_1)
        else : pass


