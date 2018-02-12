import re

p1 = re.compile("Crow|Servo")
m1 = p1.match("CrowHello")
print("m1 : ", m1)

p2 = re.compile("^Life")
p3 = re.compile("Life$")
m2 = p2.search("Life is too short")
m3 = p2.search("My Life")
m4 = p3.search("My Life")
print("m2 : ", m2)
print("m3 : ", m3)
print("m4 : ", m4)

p4 = re.compile(r"\bclass\b")
m5 = p4.search("no class at all")
print("m5 : ", m5)

p5 = re.compile(r"(\b\w+)\s+\1")
m6 = p5.search("Paris in the the spring").group()
print("m6 : ", m6)

data = """김상엽 010-2050-3863
김건홍 010-1234-5678
전수범 010-010-010
남시언 010-5574-2125"""

test1 = re.compile(r"(?P<name>\w+)\s+(?P<phone_number>\d+[-]\d+[-]\d+)")
print("test1.findall : ", test1.findall(data))
print("test1.finditer : ", test1.finditer(data))
for item in test1.finditer(data) :
    print("name : %s\tphone_number : %s" %(item.group("name"), item.group("phone_number")))

test2 = re.compile(r"(?P<name>\w+)\s+(?P<number>\d+)[-](?P=number)[-](?P=number)")
print(test2.search(data))

test3 = re.compile(r"김상엽\s+.+")
print(test3.search(data).group())