import pandas as pd

a = pd.DataFrame([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
s = pd.Series([1.0, 3, 5, 7, 9])
tbl_1 = pd.DataFrame({"weight" : [80.0, 70.4, 65.5, 45.9, 51.2], "height" : [170, 180, 155, 143, 154], "type" : ['f', 'n', 'n', 't', 't']})
tbl_2 = pd.DataFrame({"weight" : [80.0, 70.4, 65.5, 45.9, 51.2, 72.5], "height" : [170, 180, 155, 143, 154, 160], "gender" : ['f', 'm', 'm', 'f', 'f', 'm']})
tbl_3 = tbl_1[["weight", "height"]]
tbl_3 = tbl_3.append({"weight" : 72.5, "height" : 160}, ignore_index=True)
print(tbl_3)
print(tbl_1[["weight", "height"]])

# print(a)
# print()
# print(s)
# print()
#
# print("List of weight")
# print(tbl_1["weight"])
# print()
# print("List of weight and height")
# print(tbl_1[["weight", "height"]])
# print()
# print("tbl[2:4]\n", tbl_1[2:4])
# print("tbl[3:]\n", tbl_1[3:])
# print()
# print("heiger than 160")
# print(tbl_2[tbl_1.height > 160])
# print("only m")
# print(tbl_2[tbl_1.gender == 'm'])