#coding=utf-8
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

team_code="1419"

df = pd.read_csv(team_code + ".csv")
train, test = df.iloc[1:150,:], df.iloc[150:200,:]
y_train, X_train = train["funny_rating"], train.drop(["funny_rating", "stars", "unkown"], axis = 1)
X_test = test.drop(["funny_rating", "stars", "unkown"], axis = 1)

model = RandomForestClassifier(n_estimators=50, criterion="gini",max_features="sqrt",min_samples_leaf=1,n_jobs=4)
model.fit(X_train, y_train)

predict_tmp = model.predict(X_test)
test_success = 0
test_fail = 0
for j,k in zip(predict_tmp, test["funny_rating"]):
    if j == k:
        test_success = test_success + 1
    else:
        test_fail = test_fail + 1
print test_success
print test_fail
d = zip(X_train.columns, model.feature_importances_)
d = dict(d)
print sorted(d.items(), key=lambda item:item[1])
