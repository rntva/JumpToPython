import sys

def greet_users(str_list) :
    for x in str_list :
        temp2 = ""
        temp = list(x)
        temp1 = str(temp[0]).upper()
        for y in temp[1:] :
            temp2 += y
        print("Hello, %s!" %(temp1+temp2))

usernames = sys.argv[1:]
greet_users(usernames)