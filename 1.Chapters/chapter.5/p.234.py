list_a = ["is", "am", "are"]

list_a.insert(0, "ho~u")

print(list_a)

print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])))
print(list(map(lambda x : x * 2, [1,2,3,4,5,6,7,8,9,10])))