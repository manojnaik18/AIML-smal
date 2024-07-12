import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

msg = pd.read_csv('document.csv', names=['message', 'label'])
print("Total Instances of Dataset:", msg.shape[0])
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})

X = msg.message
y = msg.labelnum
print(X)
print(y)

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)
print("\nTotal number of training data:", ytrain.shape[0])
print("Total number of test data:", ytest.shape[0])

count_v = CountVectorizer()
Xtrain_dm = count_v.fit_transform(Xtrain)
Xtest_dm = count_v.transform(Xtest)

print("\nWords or tokens in text document:")
print(count_v.get_feature_names_out())

clf = MultinomialNB()
clf.fit(Xtrain_dm, ytrain)

pred = clf.predict(Xtest_dm)
print('Accuracy:', accuracy_score(ytest, pred))
print('Precision:', precision_score(ytest, pred))
print('Recall:', recall_score(ytest, pred))
print('Confusion Matrix:\n', confusion_matrix(ytest, pred))
