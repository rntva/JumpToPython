import re

p1 = re.compile("[a-z]+")
m1 = p1.match("python")
m2 = re.match("[a-z]+", "python")
print("m1과 m2는 같은 표현이다. : ", end='')
print(m1, m2)

p2 = re.compile("a.b")
m3 = p2.match("a\nb")
print(m3)
p3 = re.compile("a.b", re.DOTALL)
m4 = p3.match("a\nb")
print(m4)

p4 = re.compile("[a-z]+", re.IGNORECASE)
m5 = p4.match("python")
print(m5)
m6 = p4.match("Python")
print(m6)
m7 = p4.match("PYTHON")
print(m7)

p5 = re.compile("^python\s\w+")
p6 = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""
print(p5.findall(data))
print(p6.findall(data))