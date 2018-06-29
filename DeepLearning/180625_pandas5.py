import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("http://qrc.depaul.edu/Excel_Files/WorldOilProduction.xls")
Oil_dict = {}

for key in df :
    Oil_dict[key] = []

for key in Oil_dict.keys() :
    Oil_dict[key].append(list(df[key]))

print(Oil_dict)

# keys = list(Oil_dict.keys())
# print(keys[0])
# print(list(df[keys[0]]))

# years = df["Annual World Oil Production"][4:]
# production = df["Unnamed: 1"][4:]
# print(df["Annual World Oil Production"])
# print(df["Unnamed: 1"])


# plt.plot(years, production)
# plt.show()

