from sklearn import  ensemble, metrics
import numpy as np
import pandas as pd
"""
train_data = np.loadtxt('ML_HW6/hw6_train.dat.txt')
train_X, train_y = train_data[:,:-1], train_data[:,-1]

test_data = np.loadtxt('ML_HW6/hw6_test.dat.txt')
test_X, test_y = test_data[:,:-1], test_data[:,-1]

forest = ensemble.RandomForestClassifier(n_estimators = 100, max_depth = 200, min_samples_split = 2)
forest_fit = forest.fit(train_X, train_y)

test_y_predicted = forest.predict(test_X)
accuracy = metrics.accuracy_score(test_y, test_y_predicted)
"""
data = pd.read_csv('data_tele.csv')
print(data.info)
data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
print(data.info)
