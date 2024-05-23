import csv
import random
from virtual_assets import VIRTUAL_EPL_TEAMS_ENCODED

print("Importing sklearn modules... \n")
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.multioutput import MultiOutputClassifier
# from sklearn.ensemble import RandomForestClassifier



# model = Perceptron()
# model = svm.SVC() 
model = KNeighborsClassifier(n_neighbors=5)
# model = GaussianNB()


# Read data in file and convert team names to vector representation
print("Reading data from file... \n")
with open("vff.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        # cr = {
        #     "evidence": [cell for cell in row[:17]],
        #     "label": [cell for cell in row[17:]],
        # }
        print("Label: ", int(f"{row[17]}{row[18]}"))
        cr = {
            "evidence": [],
            "label":  int(f"{row[17]}{row[18]}"),
        }
        home_team = VIRTUAL_EPL_TEAMS_ENCODED[row[0]] 
        away_team = VIRTUAL_EPL_TEAMS_ENCODED[row[1]]
        
        
        # cr['evidence'].append(home_team)
        # cr['evidence'].append(away_team)
        # cr['evidence']= cr['evidence']+ [float(cell) for cell in row[2:17]]

        cr['evidence'] = home_team + away_team + [float(cell) for cell in row[2:17]]


        data.append(cr)


for i in data:
    print()
    print()
    print(i)



# Separate data into training and testing groups
print("Separating data into training and testing groups... \n")
holdout = int(0.20 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

# Train model on training set
print("Training... \n")
X_training = [row["evidence"] for row in training]
y_training = [row["label"] for row in training]
model.fit(X_training, y_training)

# Make predictions on the testing set
print("Predicting... \n")
X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)

# Compute how well we performed
print("Computing accuracy... \n")
correct = 0
incorrect = 0
total = 0

# Check if the digits as two
# Check if 
#
#

for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1

    print("Actual: ", actual, "----", "Predicted: ", predicted)

# # Print results
# print(f"Results for model {type(model).__name__}")
# print(f"Correct: {correct}")
# print(f"Incorrect: {incorrect}")
# print(f"Accuracy: {100 * correct / total:.2f}%")

