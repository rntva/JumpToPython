import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
#데이터 읽기
mr = pd.read_csv("mushroom.csv", header=None)
#데이터 내부의 기호를 숫자로 변환하기
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows() :
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:] :
        row_data.append(ord(v))
    data.append(row_data)
#학습 전용 데이터, 데스트 전용 데이터 나누기
data_train, data_test, label_train, label_test = train_test_split(data, label)
#데이터 학습 시키기
clf = RandomForestClassifier()
clf.fit(data_train, label_train)
#데이터 예측하기
pre = clf.predict(data_test)
#결과 테스트하기
ac_score = metrics.accuracy_score(label_test, pre)
cl_report = metrics.classification_report(label_test, pre)
print("정답률", ac_score)
print("리포트 =\n", cl_report)