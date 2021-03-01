# -------------------------------------------------------------------------
# AUTHOR: Calvin Ye
# FILENAME: knn.py
# SPECIFICATION: Read binary_points.csv and output the LOO-CV error rate
# FOR: CS 4200- Assignment #2
# TIME SPENT: 19 MINUTES
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

# loop your data to allow each instance to be your test set
fail = 0
total = 0
for i, instance in enumerate(db):
    # add the training features to the 2D array X removing the instance that will be used for testing in this
    # iteration. For instance, X = [[1, 3], [2, 1,], ...]] --> add your Python code here X =
    X = []
    for index, inst in enumerate(db):
        if index is not i:
            X.append([inst[0], inst[1]])

    # transform the original training classes to numbers and add to the vector Y removing the instance that will be
    # used for testing in this iteration. For instance, Y = [1, 2, ,...] --> add your Python code here Y =
    Y = []
    for index, inst in enumerate(db):
        if index is not i:
            if inst[2] == '+':
                Y.append(1)
            else:
                Y.append(2)

    # store the test sample of this iteration in the vector testSample
    # --> add your Python code here
    # testSample =
    testSample = [instance[0], instance[1]]

    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    # use your test sample in this iteration to make the class prediction. For instance:
    # class_predicted = clf.predict([[1, 2]])[0]
    # --> add your Python code here
    class_predicted = clf.predict([testSample])[0]

    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here
    if instance[2] == '+':
        true = 1
    else:
        true = 2

    if class_predicted != true:
        fail += 1
    total += 1

# print the error rate
# --> add your Python code here
print(str(fail) + "/" + str(total) + " =", (fail / total))
