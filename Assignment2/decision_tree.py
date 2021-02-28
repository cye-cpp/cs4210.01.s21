# -------------------------------------------------------------------------
# AUTHOR: Calvin Ye
# FILENAME: decision_tree.py
# SPECIFICATION: Assignment #2 Question #2: Read 3 different training sets and train/test/output performance
# FOR: CS 4200- Assignment #2
# TIME SPENT: 48 MINUTES
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    # X =
    for data in dbTraining:
        inst = []
        # AGE: YOUNG = 1 ; PREPRESBYOPIC = 2 ; PRESBYOPIC = 3
        if data[0] == 'Young':
            inst.append(1)
        elif data[0] == 'Prepresbyopic':
            inst.append(2)
        else:
            inst.append(3)

        # SPECTACLE PRESCRIPTION: MYOPE = 1 ; HYPERMETROPE = 2
        if data[1] == 'Myope':
            inst.append(1)
        else:
            inst.append(2)

        # ASTIGMATISM: YES = 1 ; NO = 2
        if data[2] == 'Yes':
            inst.append(1)
        else:
            inst.append(2)

        # TEAR PRODUCTION RATE: NORMAL = 1 ; REDUCED = 2
        if data[3] == 'Normal':
            inst.append(1)
        else:
            inst.append(2)

        # APPEND INSTANCE TO X
        X.append(inst)

    # transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    # Y =
    for data in dbTraining:
        # RECOMMEND LENSES: YES = 1 ; NO = 2
        if data[4] == 'Yes':
            Y.append(1)
        else:
            Y.append(2)

    # loop your training and test tasks 10 times here
    lowest_accuracy = None
    for i in range(10):
        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        # dbTest =
        dbTest = []
        with open(ds, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)

        tp = 0
        tn = 0
        fp = 0
        fn = 0
        total = 0
        for data in dbTest:
            # transform the features of the test instances to numbers following the same strategy done during
            # training, and then use the decision tree to make the class prediction. For instance: class_predicted =
            # clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label
            # so that you can compare it with the true label --> add your Python code here
            inst = []
            training = []
            # AGE: YOUNG = 1 ; PREPRESBYOPIC = 2 ; PRESBYOPIC = 3
            if data[0] == 'Young':
                inst.append(1)
            elif data[0] == 'Prepresbyopic':
                inst.append(2)
            else:
                inst.append(3)

            # SPECTACLE PRESCRIPTION: MYOPE = 1 ; HYPERMETROPE = 2
            if data[1] == 'Myope':
                inst.append(1)
            else:
                inst.append(2)

            # ASTIGMATISM: YES = 1 ; NO = 2
            if data[2] == 'Yes':
                inst.append(1)
            else:
                inst.append(2)

            # TEAR PRODUCTION RATE: NORMAL = 1 ; REDUCED = 2
            if data[3] == 'Normal':
                inst.append(1)
            else:
                inst.append(2)

            training.append(inst)
            prediction = clf.predict(training)[0]
            # print(prediction)

            # compare the prediction with the true label (located at data[4]) of the test instance to start
            # calculating the accuracy. --> add your Python code here
            if data[4] == 'Yes' and prediction == 1:
                # TRUE POSITIVE
                tp += 1
            elif data[4] == 'No' and prediction == 2:
                # TRUE NEGATIVE
                tn += 1
            elif data[4] == 'No' and prediction == 1:
                # FALSE POSITIVE
                fp += 1
            elif data[4] == 'Yes' and prediction == 2:
                # FALSE NEGATIVE
                fn += 1
            else:
                print("unknown result")
            total += 1

        # find the lowest accuracy of this model during the 10 runs (training and test set)
        # --> add your Python code here
        test_accuracy = (tp + tn) / total
        if lowest_accuracy is None or test_accuracy < lowest_accuracy:
            lowest_accuracy = test_accuracy

    # print the lowest accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that:
    #   final accuracy when training on contact_lens_training_1.csv: 0.2
    #   final accuracy when training on contact_lens_training_2.csv: 0.3
    #   final accuracy when training on contact_lens_training_3.csv: 0.4
    # --> add your Python code here
    print("final accuracy when training on", ds, ":", lowest_accuracy)
