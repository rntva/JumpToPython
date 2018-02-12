a = []
c = []

for x in range(1,101) :
    a.append('a'+str(x))

for x in range(1,101) :
    a.append('b'+str(x))

for x in range(int(len(a)/2)) :
    c.append(a[x])
    c.append(a[x+int(len(a)/2)])

print(c)