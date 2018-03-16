#!/usr/bin/env python3

import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

iris = pd.read_csv("irisaa.csv", sep=',', header=0)
print(iris)
iris["variety01"] = np.where(iris["variety"] == "Setosa", 1., 0.)
# print(iris.head())

#-------------------------------------------------------------------------------------------------
csv_data = iris[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
csv_label = iris["variety01"]
# print(csv_label)
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)
clf = svm.SVC()
clf.fit(train_data, train_label)
#-------------------------------------------------------------------------------------------------

print("\t\t그룹별 기술통계 구하기")
print(iris.groupby(["variety"])[["sepal.length", "sepal.width", "petal.length", "petal.width"]].agg(["count", "mean", "std"]))

check = iris.groupby(["variety"])[["sepal.length", "sepal.width", "petal.length", "petal.width"]].agg(["count", "mean", "std"])

print("\n\t\t별수별 서로 다른 통계량 구하기")
print(iris.groupby(["variety"]).agg({"sepal.length" : ["count", "mean", "std"],
                                  "sepal.width" : ["mean", "std"],
                                  "petal.length" : ["mean", "std"],
                                  "petal.width" : ["mean", "std"]}))

check = iris.groupby(["variety"]).agg({"sepal.length" : ["count", "mean", "std"],
                                  "sepal.width" : ["mean", "std"],
                                  "petal.length" : ["mean", "std"],
                                  "petal.width" : ["mean", "std"]})
print(check.values[0][0])

dependent_variable = iris["variety01"]
independent_variables = iris[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
independent_variables_withconstant= sm.add_constant(independent_variables, prepend=True)
logit_model = sm.Logit(dependent_variable, independent_variables_withconstant).fit_regularized()


print("\nQuantities you can extract from the result :\n%s" %dir(logit_model))
print("\nCoefficients :\n%s" %logit_model.params)
print("\nCoefficient Std Errors :\n%s" %logit_model.bse)

print("예측")
# new_observations = iris.ix[iris.index.isin([2, 42, 55, 78, 105, 144]), independent_variables.columns]
random_index = random.sample(range(1,150), 10)
temp_data = []
temp_label = []
for index in random_index :
    temp_data.append(csv_data.ix[index, :])
    temp_label.append(csv_label.ix[index])
pre = clf.predict(temp_data)
pre = list(map(float, pre))
new_observations = iris.ix[iris.index.isin(random_index), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)
print(pre)
# print(temp_label)
print(random_index)

ac_score_lo = metrics.accuracy_score(temp_label, y_predicted_rounded)
ac_score_svc = metrics.accuracy_score(temp_label, pre)
print("ac_score_logistics : ", ac_score_lo)
print("ac_score_svc : ", ac_score_svc)

print("end")