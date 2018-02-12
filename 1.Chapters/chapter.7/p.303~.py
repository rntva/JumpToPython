import re
p = re.compile("[a-z]+")

m = p.match("python")
print(m)
print(m.span())

# m = p.match("3 python")
print("Match Found:", m.group(), m)

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

result = p.findall("life is too short.")
print(result)

result = p.finditer("life is too short.")
print(result)

for x in result : print(x)