import re

p = re.compile("a.b")
m = p.match("a\nb")
print(m)
print("-------------------------------------------------")
pp = re.compile("a.b", re.S)
m = pp.match("a\nb")
print(m)
print("-------------------------------------------------")
p = re.compile("[a-z]")
pp = re.compile("[a-z]", re.I)
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))
print(pp.match("python"))
print(pp.match("Python"))
print(pp.match("PYTHON"))
print("-------------------------------------------------")
p = re.compile("[a-z]+")
pp = re.compile("[a-z]+", re.I)
print(p.match("python12"))
print(p.match("Python22"))
print(p.match("PYTHON242"))
print(pp.match("py4thon3"))
print(pp.match("Python4"))
print(pp.match("PYTHON5"))

print("-------------------------------------------------")
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

print("-------------------------------------------------")
pp = re.compile("^python\s\w{4,}", re.M)

data = """python one
life is too short
python two
you need python
python three"""

print(pp.findall(data))