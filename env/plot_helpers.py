import matplotlib.pyplot as plt
import numpy as np

#average passanger class is better with higher age
def plotAgesAndPClass(df):
    average_pclass_by_age = df.groupby('Age')['Pclass'].mean().to_dict()
    ages = []
    average_pclass = []

    for age, pclass in average_pclass_by_age.items():
        ages.append(age)
        average_pclass.append(pclass)

    xpoints = np.array(ages)
    ypoints = np.array(average_pclass)
        
    plt.plot(xpoints, ypoints, 'o-')  # 'o-' for points connected by lines
    plt.xlabel('Age')
    plt.ylabel('Average Pclass') 
    plt.title('Average Pclass by Age') 
    plt.show()

#middle age people less likely to survive
def plotAgesAndSurvivability(df):
    average_surv_by_age = df.groupby('Age')['Survived'].mean().to_dict()
    ages = []
    average_surv = []

    for age, surv in average_surv_by_age.items():
        ages.append(age)
        average_surv.append(surv)

    xpoints = np.array(ages)
    ypoints = np.array(average_surv)
        
    plt.plot(xpoints, ypoints, 'o-')  # 'o-' for points connected by lines
    plt.xlabel('Age')
    plt.ylabel('Average survived') 
    plt.title('Average Survivability by Age') 
    plt.show()
    
#this seems random
def plotFareAndSurvivability(df):
    average_surv_by_fare = df.groupby('Fare')['Survived'].mean().to_dict()
    fares = []
    average_surv = []

    for fare, surv in average_surv_by_fare.items():
        if fare <=100:
            fares.append(fare)
            average_surv.append(surv)

    xpoints = np.array(fares)
    ypoints = np.array(average_surv)
        
    plt.plot(xpoints, ypoints, 'o-')  # 'o-' for points connected by lines
    plt.xlabel('Fare')
    plt.ylabel('Average survived') 
    plt.title('Average Survivability by Fare') 
    plt.show()
    
#higher class = better odds
def plotClassAndSurvivability(df):
    average_surv_by_class = df.groupby('Pclass')['Survived'].mean().to_dict()
    classes = []
    average_surv = []

    for clas, surv in average_surv_by_class.items():
        classes.append(clas)
        average_surv.append(surv)

    xpoints = np.array(classes)
    ypoints = np.array(average_surv)
        
    plt.plot(xpoints, ypoints, 'o-')  # 'o-' for points connected by lines
    plt.xlabel('Class')
    plt.ylabel('Average survived') 
    plt.title('Average Survivability by Class') 
    plt.show()

#B, D and E cabins seem to have better chance of surviving
def plotCabinLetterAndSurvivability(df):
    df['CabinLetter'] = df['Cabin'].str[0]
    
    average_surv_by_cabin_letter = df.groupby('CabinLetter')['Survived'].mean().sort_index().to_dict()
    
    # Extract cabin letters and their corresponding average survivability
    cabin_letters = list(average_surv_by_cabin_letter.keys())
    average_surv = list(average_surv_by_cabin_letter.values())
    
    # Convert lists to numpy arrays for plotting
    xpoints = np.array(cabin_letters)
    ypoints = np.array(average_surv)
    
    # Plotting
    plt.plot(xpoints, ypoints, 'o-')  # 'o-' for points connected by lines
    plt.xlabel('Cabin Letter')
    plt.ylabel('Average Survivability') 
    plt.title('Average Survivability by Cabin Letter') 
    plt.show()

#I dont see corrolation so will eddit data to only have the letter
def plotCabinNumberAndSurvivability(df):
    df['CabinNumber'] = df['Cabin'].str[1:]
    
    # Calculate the average survivability by cabin letter
    average_surv_by_cabin_letter = df.groupby('CabinNumber')['Survived'].mean().sort_index().to_dict()
    
    # Extract cabin letters and their corresponding average survivability
    cabin_letters = list(average_surv_by_cabin_letter.keys())
    average_surv = list(average_surv_by_cabin_letter.values())
    
    # Convert lists to numpy arrays for plotting
    xpoints = np.array(cabin_letters)
    ypoints = np.array(average_surv)
    
    # Plotting
    plt.plot(xpoints, ypoints, 'o-')  # 'o-' for points connected by lines
    plt.xlabel('Cabin Number')
    plt.ylabel('Average Survivability') 
    plt.title('Average Survivability by Cabin Number') 
    plt.show()
    
def runAllPlot(df):
    plotAgesAndPClass(df)
    plotAgesAndSurvivability(df)
    plotFareAndSurvivability(df)
    plotClassAndSurvivability(df)
    plotCabinLetterAndSurvivability(df)
    plotCabinNumberAndSurvivability(df)