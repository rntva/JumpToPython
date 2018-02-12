import re
import os

p1 = re.compile(".+(?=:)")
p2 = re.compile(".+(?!:)")
print(p1.search(r"http://www.google.com").group())
print(p2.search(r"http://www.google.com").group())

test1 = re.compile(r".+[.](?!exe$|DBF$).+")
D_dir_list = os.listdir("D:\\")
print(D_dir_list)

for file_name in D_dir_list :
    if os.path.isfile("D:\\"+file_name) :
        if test1.search(file_name) != None :
            print(test1.search(file_name).group())
        elif test1.search(file_name) == None :
            print("%s는 .exe 또는 .DBF 파일이라 제외되었다." %file_name)

p3 = re.compile(r"(blue|red|white)")
print(p3.sub("color", "blue socks and red shoes"))
print(p3.sub("color", "blue socks and red shoes", count=1))

p4 = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
print(p4.sub("\g<phone> \g<name>", "김상엽 010-2050-3863"))
print(p4.sub("\g<2> \g<1>", "김상엽 010-2050-3863"))

def deci_to_hex(match) :
    value = int(match.group())
    return hex(value)

p5 =re.compile(r"\d+")
print(p5.sub(deci_to_hex, "call 65490 for printing, 49152 for user code."))
