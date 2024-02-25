#licensed under an Open Source Initiative-approved license (see www.opensource.org)
import pandas as pd
from plot_helpers import runAllPlot
import ai_helpers as a
import warnings

# Suppressing PerformanceWarning
warnings.filterwarnings('ignore', category=pd.errors.PerformanceWarning)


train_path = 'training_data.csv'
test_path = 'testing_data.csv'
potentialColumns = ['Ticket', 'Pclass', 'Sex', 'Embarked', 'CabinLetter', 'Parch', 'Age', 'SibSp', 'Fare']

a.trainTestSplit()

df = pd.read_csv(train_path)

#runAllPlot(df)

#get single best column
# for trainColumns in potentialColumns:
#     trainColumns = [trainColumns]
#     print(trainColumns, a.runAI(df, trainColumns))

# #using the 3 most representative columns
# represent3 = ["Fare", "Sex", "Pclass"]
# print(represent3, a.runAI(df, represent3))

# #using the 5 most representative columns
# represent5 = ["Fare", "Sex", "Pclass", "Ticket", "CabinLetter"]
# print(represent5, a.runAI(df, represent5))

#this will take a lil while
# results = {}
# for i in range(1, 9):
#     for combination in a.generate_combinations(potentialColumns, i):
#         results[', '.join(combination)] = a.runAI(df, combination)

# sorted_dict = dict(sorted(results.items(), key=lambda item: item[1]))
# print(sorted_dict)

#To test positives/negatives goto ai_helpers -> testAIModel and uncomment
best = ['Ticket', 'Pclass', 'Sex', 'Parch', 'Fare']
print(best, a.runAI(df, best))
