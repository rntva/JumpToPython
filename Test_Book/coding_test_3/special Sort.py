int_list = [-2,3,4,-1,-3,-6,-5,7,8,5,10]
int_minus = []
int_plus = []
for x in int_list :
    if x >= 0 : int_plus.append(x)
    elif x < 0 : int_minus.append(x)
result = int_minus + int_plus
print(result)

