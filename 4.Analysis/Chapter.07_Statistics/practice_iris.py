#!/usr/bin/env python3

import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

iris = pd.read_csv("iris.csv", sep=',', header=0)
print(iris)
iris["variety01"] = np.where(iris["variety"] == "Setosa", 1., 0.)
# print(iris.head())

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
new_observations = iris.ix[iris.index.isin(random.sample(range(1,150), 10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)

print("end")