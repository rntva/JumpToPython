import re

p = re.compile("[a-z]+")

m1 = p.match("python")
print(m1)

m2 = p.match("3 python")
print(m2)

m3 = p.search("python")
print(m3)

m4 = p.search("3 python")
print(m4)

m5 = p.findall("life is too short")
print(m5)

m6 = p.finditer("life is too short")

print(m1.group())
print(m1.start())
print(m1.end())
print(m1.span())