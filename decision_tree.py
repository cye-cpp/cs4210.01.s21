# -------------------------------------------------------------------------
# AUTHOR: Calvin Ye
# FILENAME: decision_tree.py
# SPECIFICATION: Reads contact_lens.csv and outputs a decision tree of ID3
# FOR: CS 4200- Assignment #1
# TIME SPENT: 12 MINUTES
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original training features to numbers and add to the 4D array X. For instance Young = 1,
# Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]] --> add your Python code here X =
for data in db:
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

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2,
# so Y = [1, 1, 2, 2, ...] --> add your Python code here Y =
for data in db:
    # RECOMMEND LENSES: YES = 1 ; NO = 2
    if data[4] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes', 'No'], filled=True,
               rounded=True)
plt.show()
