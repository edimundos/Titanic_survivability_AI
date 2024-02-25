import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from itertools import combinations
from sklearn.metrics import confusion_matrix

original = 'train.csv'
train_path = 'training_data.csv'
test_path = 'testing_data.csv'

def trainTestSplit():
    df = pd.read_csv(original)
    df = prepData(df)
    train_df, test_df = train_test_split(df, test_size=0.25, random_state=42)
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
def prepData(df):
    df['Age'] = df['Age'].round()
    
    fill_values = {'Cabin': 'Missing', 'Age': 'Missing'}
    for col, value in fill_values.items():
        df[col] = df[col].fillna(value)
        
    df['CabinLetter'] = df['Cabin'].str[0]
    return df

def getDummiesByColumns(df, columns, dummiesTrain=None):
    dummies = pd.get_dummies(df, columns=columns)
    columns_list = df.columns.tolist()
    for column in columns:
        if column in columns_list:
            columns_list.remove(column)
        
    columns_list.remove('Survived')
    dummies = dummies.drop(columns_list, axis=1)
        
    return dummies

def getAIModel(dummies):
    feature_columns = dummies.columns.tolist()
    feature_columns.remove('Survived')
    x_train = dummies[feature_columns]
    y_train = dummies['Survived']

    # Creating the RandomForestClassifier instance
    clf = RandomForestClassifier(random_state=42)

    # Training the model
    clf.fit(x_train, y_train)
    return clf

def getMissingColumns(dummies, otherDummies):
    
    for column in otherDummies.columns:
            if column not in dummies.columns:
                dummies[column] = False
                
    dummies = dummies.sort_index(axis=1)
        
    return dummies
    

def testAIModel(testDummies, clf):  
    x_test = testDummies.drop(['Survived'], axis=1)
    y_test = testDummies['Survived']
    predictions = clf.predict(x_test)

    # uncomment this to see AI's predictions
    # for i, prediction in enumerate(predictions):
    #     actual = y_test[i]
    #     is_correct = 'Correct' if prediction == actual else 'Incorrect'
    #     print(f"Prediction: {prediction}, Actual: {actual}, Result: {is_correct}")
    #     test_row = x_test.iloc[i]
    #     true_columns = test_row[test_row == 1].index.tolist()
    #     print("True columns:", true_columns)
    #     print("\n")

    correct_predictions = (predictions == y_test).sum()
    accuracy = correct_predictions / len(predictions)
    return accuracy

def runAI(df, trainColumns):
    dummies = getDummiesByColumns(df, trainColumns)

    testDF = pd.read_csv(test_path)
    testDF= prepData(testDF)
    testDummies = getDummiesByColumns(testDF, trainColumns, dummies)

    dummies = getMissingColumns(dummies, testDummies)
    testDummies = getMissingColumns(testDummies, dummies)

    clf = getAIModel(dummies)
    return testAIModel(testDummies, clf)

def generate_combinations(items, n):
    return [list(comb) for comb in combinations(items, n)]