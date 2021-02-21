# -------------------------------------------------------------------------
# AUTHOR: Calvin Ye
# FILENAME: find_s.py
# SPECIFICATION: Reads contact_lens.csv and output hypothesis of Find-S algorithm
# FOR: CS 4200- Assignment #1
# TIME SPENT: 14 MINUTES
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard vectors and arrays

# importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes  # representing the most specific possible hypothesis
print(hypothesis)

# find the first positive training data in db and assign it to the vector hypothesis
data = None
while len(db) > 0:
    data = db.pop(0)
    if data[4] == 'Yes':
        # FIRST POSITIVE DATA FOUND, ASSIGN TO HYPOTHESIS
        hypothesis = [data[0], data[1], data[2], data[3]]
        break

# find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis
# (special characters allowed: "0" and "?")
while len(db) > 0:
    data = db.pop(0)
    if data[4] == 'Yes':
        # COMPARE DATA
        if hypothesis[0] != data[0]:
            hypothesis[0] = '?'
        if hypothesis[1] != data[1]:
            hypothesis[1] = '?'
        if hypothesis[2] != data[2]:
            hypothesis[2] = '?'
        if hypothesis[3] != data[3]:
            hypothesis[3] = '?'

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)
