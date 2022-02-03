######  Logistic Regression  ######
from sklearn.linear_model import LogisticRegressionCV
model = LogisticRegressionCV(cv=5, random_state=1, max_iter=5000)
'''
[('Age', -0.9416922216222768),
 ('Gender', 2.2461606354415915),
 ('Class', 0.4581024152686117),
 ('Married', 0.13423592334511097),
 ('Fare', 0.6312702308180135),
 ('Joined_Cherbourg', -0.03488208118960456),
 ('Joined_Queenstown', -1.053185674506751),
 ('Joined_Southampton', -0.5322053381169515)]

model.score(x_trained_numpy, y_train_numpy)
=> 0.7865232163080408

model.score(x_test_numpy, y_test_numpy)
=> 0.7647058823529411
'''
