from sklearn import tree
#Using DecisionTree classifier for prediction
clf = tree.DecisionTreeClassifier()
#Here the array contains three values which are height,weight and shoe size
X = [[220701082], [220801082],[220801000],[220701000]]
Y = ['cse', 'bio', 'bio', 'cse' ]
clf = clf.fit(X, Y)
#Predicting on basis of given random values for each given feature
cs = clf.predict([[220701111]])
bio = clf.predict([[220801072]])
#Printing final prediction
print(cs)
print(bio)