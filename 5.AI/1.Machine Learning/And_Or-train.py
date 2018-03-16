import pandas as pd
from sklearn import svm, metrics

and_input = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

or_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

and_data = []
and_label = []
for row in and_input :
    p = row[0]
    q = row[1]
    r = row[2]
    and_data.append([p, q])
    and_label.append(r)

or_df = pd.DataFrame(or_input)
or_data = or_df.ix[:, 0:1]
or_label = or_df.ix[:, 2]

and_clf = svm.SVC()
and_clf.fit(and_data, and_label)

or_clf = svm.SVC()
or_clf.fit(or_data, or_label)

and_pre = and_clf.predict(and_data)
or_pre = or_clf.predict(or_data)
print("And_예측결과 : ", and_pre)
print("Or_예측결과 : ", or_pre)

and_ac_score = metrics.accuracy_score(and_label, and_pre)
print("정답률", and_ac_score)

or_ac_score = metrics.accuracy_score(or_label, or_pre)
print("정답률", or_ac_score)