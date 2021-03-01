# -------------------------------------------------------------------------
# AUTHOR: Calvin Ye
# FILENAME: naive_bayes.py
# SPECIFICATION: Reads weather_training.csv and outputs classification of each test instance
# FOR: CS 4200- Assignment #2
# TIME SPENT: 16 MINUTES
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard vectors and arrays

# importing some Python libraries
import csv

from sklearn.naive_bayes import GaussianNB

db = []

# reading the training data
# --> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

# transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast =
# 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]] --> add your Python code here X =
X = []
for data in db:
    inst = []
    # OUTLOOK: SUNNY = 1 ; OVERCAST = 2 ; RAIN = 3
    if data[1] == 'Sunny':
        inst.append(1)
    elif data[1] == 'Overcast':
        inst.append(2)
    else:
        inst.append(3)

    # TEMPERATURE: HOT = 1 ; MILD = 2 ; COOL = 3
    if data[2] == 'Hot':
        inst.append(1)
    elif data[2] == 'Mild':
        inst.append(2)
    else:
        inst.append(3)

    # HUMIDITY: NORMAL = 1 ; HIGH = 2
    if data[3] == 'Normal':
        inst.append(1)
    else:
        inst.append(2)

    # WIND: WEAK = 1 ; STRONG = 2
    if data[3] == 'Weak':
        inst.append(1)
    else:
        inst.append(2)

    X.append(inst)

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2,
# so Y = [1, 1, 2, 2, ...] --> add your Python code here Y =
Y = []
for data in db:
    if data[5] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in a csv file
# --> add your Python code here
dbTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)

# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(
    15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

# use your test samples to make probabilistic predictions.
# --> add your Python code here
# -->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for data in dbTest:
    inst = []
    # OUTLOOK: SUNNY = 1 ; OVERCAST = 2 ; RAIN = 3
    if data[1] == 'Sunny':
        inst.append(1)
    elif data[1] == 'Overcast':
        inst.append(2)
    else:
        inst.append(3)

    # TEMPERATURE: HOT = 1 ; MILD = 2 ; COOL = 3
    if data[2] == 'Hot':
        inst.append(1)
    elif data[2] == 'Mild':
        inst.append(2)
    else:
        inst.append(3)

    # HUMIDITY: NORMAL = 1 ; HIGH = 2
    if data[3] == 'Normal':
        inst.append(1)
    else:
        inst.append(2)

    # WIND: WEAK = 1 ; STRONG = 2
    if data[3] == 'Weak':
        inst.append(1)
    else:
        inst.append(2)

    predicted = clf.predict_proba([inst])[0]
    if predicted[0] > predicted[1]:
        playTennis = "Yes"
        confidence = predicted[0]
    else:
        playTennis = "No"
        confidence = predicted[1]

    # PRINT ONLY IF CONVIDENCE IS >= 0.75
    if confidence >= 0.75:
        print(data[0].ljust(15) + data[1].ljust(15) + data[2].ljust(15) + data[3].ljust(15) + data[4].ljust(
            15) + playTennis.ljust(15) + str(confidence).ljust(15))
