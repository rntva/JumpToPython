import os

def get_list_sub_directory(str_in) :
    os.chdir(str_in)
    f = os.listdir(str_in)

    for x in f :
        try :
            new_name = str_in+"\\"+x
            if os.path.isdir(new_name) :
                get_list_sub_directory(new_name)
            elif os.path.splitext(x)[-1] == ".py" : print(new_name)
        except : None




# def get_list_sub_directory(str_in) :
#     os.chdir(str_in)
#     f = os.listdir(str_in)
#     for x in f :
#         try :
#             get_list_sub_directory(str_in+"\\"+x)
#         except :
#             if x.split('.')[-1] == "py" :
#                 path = os.getcwd()
#                 print(path+'\\'+x)
#             else : None

# ------------------------------------------------------------------------

# def get_list_sub_directory(str_in) :
#     os.chdir(str_in)
#     f = os.listdir(str_in)
#     ff = glob.glob(str_in+"\\*")
#     for x in ff :
#         if x.split("\\\\")[-1]


target_directory = input("검색하고 싶은 디렉토리의 경로를 설정해주십시오. : ")
get_list_sub_directory(target_directory)

# print("-----------------------------------------------------------------------------")
#
# for (path, dir, files) in os.walk(target_directory) :
#     for file_name in files :
#         ext = os.path.splitext(file_name)[-1]
#         if ext == '.py' : print(path+"\\"+file_name)