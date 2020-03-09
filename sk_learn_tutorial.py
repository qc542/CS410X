from sklearn import datasets
from sklearn import svm
iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)
print(digits.target)
print(digits.images[0])

# Fitting the model to a set of handwritten digits
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])

# Saving a model in scikit-learn by pickle & reloading it
clf = svm.SVC()
X, y = datasets.load_iris(return_X_y=True)
clf.fit(X, y)

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
print(clf2.predict(X[0:1]))
print(y[0])

# Alternatively using joblib to replace pickle
from joblib import dump, load
dump(clf, 'filename.joblib') # Pickling to the local disk
clf = load('filename.joblib') # Reloading

# Input is cast to float64 by default
import numpy as np
from sklearn import random_projection

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
print(X.dtype)

transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
# X used to be float32 but is now cast to float64 by fit_transform(X)
print(X_new.dtype)

# Regression targets are cast to float64, whereas classification targets
# are maintained
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)
print(list(clf.predict(iris.data[:3])))
# (Above) Prints an integer array because iris.target was used in clf.fit()
clf.fit(iris.data, iris.target_names[iris.target])
print(list(clf.predict(iris.data[:3])))
# (Above) Prints a string array because iris.target_names was used

# Calling fit() a second time overwrites the previously-trained model
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
clf = SVC()
print(clf.set_params(kernel='linear').fit(X, y))
# (Above) Changed to the linear kernel after the estimator has been constructed
print(clf.predict(X[:5]))
print(clf.set_params(kernel='rbf').fit(X, y))
# (Above) Changed back to rbf to retrain the estimator
print(clf.predict(X[:5]))

from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

# Classifier is fit on a 1D array of multiclass labels
classif = OneVsRestClassifier(estimator=SVC(random_state=0))
# predict() returns 1D multiclass predictions
print(classif.fit(X, y).predict(X))

# Classifier is fit on a 2D array
y = LabelBinarizer().fit_transform(y)
# predict() returns 2D multiclass predictions
print(classif.fit(X, y).predict(X))

# Fitting the classifier upon instances each assigned multiple labels
from sklearn.preprocessing import MultiLabelBinarizer
# MultiLabelBinarizer binarizes the 2D array of multilabels pointed to by y
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
print(classif.fit(X, y).predict(X))
# Returns a 2D array with multiple predicted labels for each instance