#coding=utf-8
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("166.csv")
train, test = df.iloc[1:150,:], df.iloc[151:199,:]
y_train, X_train = train["funny_rating"], train.drop(["funny_rating"], axis = 1)
X_test = test.drop(["funny_rating"], axis = 1)

model = RandomForestClassifier(n_estimators=50, criterion="gini",max_features="sqrt",min_samples_leaf=1,n_jobs=4)
model.fit(X_train, y_train)

#predict_tmp = model.predict(X_test)
#test_success = 0
#test_fail = 0
#for j,k in zip(predict_tmp,test["funny_rating"]):
#    if j == k:
#        test_success = test_success + 1
#    else:
#        test_fail = test_fail + 1
#print test_success
#print test_fail
print model.predict([10, 2, 0, 54.4, 16.2, 5, 538, 446.54, 6.94])
print zip(X_train.columns, model.feature_importances_)
