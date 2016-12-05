#coding=utf-8
import pandas as pd
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier

team_code="26"

df = pd.read_csv(team_code + ".csv")
data_lines = len(df)
train, test = df.iloc[1:data_lines - 50,:], df.iloc[data_lines - 50:data_lines,:]
test_2 = df.iloc[1:data_lines,:]
X_test_2 = test_2.drop(["funny_rating","unkown"], axis = 1)
y_train, X_train = train["funny_rating"], train.drop(["funny_rating", "unkown"], axis = 1)
X_test = test.drop(["funny_rating", "unkown"], axis = 1)

model = RandomForestClassifier(n_estimators=100, criterion="gini",max_features="sqrt",min_samples_leaf=1,n_jobs=4)
model.fit(X_train, y_train)

predict_tmp = model.predict(X_test)
test_success = 0
for j,k in zip(predict_tmp, test["funny_rating"]):
    if j == k:
        test_success = test_success + 1
print "success_rating : " + str(test_success/50.0000)
d = zip(X_train.columns, model.feature_importances_)
d = dict(d)
print sorted(d.items(), key=lambda item:item[1])

#export_graphviz(model.tree_,
#                out_file='tree.dot',
#                feature_names=df.columns,
#                max_depth=None,
#                # 下面几个参数，需要使用最新的scikit-learn 0.17版本才能用
#                class_names=["more than 3 goals", "less than 3 goals"],
#                rounded=True,
#                filled=True,
#            )
