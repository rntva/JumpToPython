import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

housing_file_path = "housing.csv"
housing = pd.read_csv(housing_file_path)

housing["housing_driveway"] = np.where(housing["driveway"] == "yes", 1., 0.)
housing["housing_recroom"] = np.where(housing["recroom"] == "yse", 1., 0.)
housing["housing_recroom"] = np.where(housing["fullbase"] == "yse", 1., 0.)
housing["housing_gashw"] = np.where(housing["gashw"] == "yse", 1., 0.)
housing["housing_airco"] = np.where(housing["airco"] == "yse", 1., 0.)
housing["housing_prefarea"] = np.where(housing["prefarea"] == "yse", 1., 0.)

housing_price_data = housing.price

housing_price_datalist = []
housing_price_predict_list = []
i = 0
while 1 :
    if i != 386 :
        housing_price_datalist.append(housing_price_data[i])
        i += 1
    else : break

housing_predictors = ["lotsize", "bedrooms", "bathrms", "stories", "housing_driveway", "housing_recroom", "housing_recroom", \
"housing_gashw", "housing_airco", "housing_prefarea"]

x = housing[housing_predictors]
y = housing_price_data
# print(x)

housing_model = DecisionTreeRegressor()
housing_model.fit(x, y)

train_data, test_data, train_label, test_label = train_test_split(x, y)
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label, pre)

t = 386
while 1 :
    if t != 546 :
        housing_price_predict_list.append(housing_model.predict(x)[t])
        t += 1
    else : break

print(housing_price_predict_list)

A = housing_price_datalist
B = housing_price_predict_list
result_value = 0
for value in [x - y for x, y in zip(A, B)] :
    result_value += value ** 2
count_value = result_value / len(A)

C = housing_price_datalist
D = pre
result_value = 0
for value in [x - y for x, y in zip(C, D)] :
    result_value += value ** 2
count_value_2 = result_value / len(C)

print("Cost Function_1 : ", count_value / 1000000, "Cost Function_2 : ", count_value_2 / 1000000)
# print("ac_score : ", ac_score)