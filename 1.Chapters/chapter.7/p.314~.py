import re

p = re.compile(r"\sclass\s")
print(p.search("No class at allclass bclassb"))

p = re.compile("(ABC)+")
m = p.search("ABCABCABCAAA OK?")
print(m)
print(m.group(0))

p = re.compile(r"(?P<name>\w+)\s+(?P<number>(\d+)[-](\d+)[-](\d+))")
m = p.search("park 010-1234-1234")
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group("name"))
print(m.group("number"))