import pandas as pd
from math import isnan

def getMedian(array):
    if (len(array) % 2):
        return(array[len(array) // 2])
    else:
        return((array[len(array) // 2] + array[len(array) // 2 - 1]) / 2)

def playWithAverages(data, cols):
    average, median, maximum, minimum = {}, {}, {}, {}
    for i in cols:
        a, validValues, values = 0, [], 0
        for j in data[i]:
            if (not isnan(j)):
                a += j
                values += 1
                validValues += [j]
        median[i] = getMedian(validValues)
        a /= values
        average[i] = a
        maximum[i] = max(validValues)
        minimum[i] = min(validValues)
    print(maximum)

    for i in cols:
        for j in range(len(data[i])):
            #if (isnan(data[i][j])):
                #data.set_value(j, i, average[i])
                #data[i][j] = median[i]
            data.set_value(j, i, (data[i][j] - minimum[i]) / (maximum[i] - minimum[i]))

def removeRows(data, cols):
    for c in cols:
        data = data[pd.isna(data[c]) != True]
    return data

data = pd.read_csv('diabetes_dataset.csv').astype('float')
cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
#
# data = removeRows(data, cols)
# print(data)
# data.to_csv("diabetes_removeAllInvalidRows_dataset.csv")
#data = pd.read_csv('diabetes_app.csv').astype('float')
playWithAverages(data, cols)
data = removeRows(data, cols)
print(data)
data.to_csv("diabetes_averageNormByMinMaxRemovingMissingValues_dataset.csv", index=False)
