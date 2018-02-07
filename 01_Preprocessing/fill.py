import pandas as pd
from math import isnan

data = pd.read_csv('diabetes_dataset.csv')
cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
res = {}
for i in cols:
    mean, values = 0, 0
    for j in data[i]:
        if (not isnan(j)):
            mean += j
            values += 1
    mean /= values
    res[i] = mean
print(res)

for i in cols:
    for j in range(len(data[i])):
        if (isnan(data[i][j])):
            data[i][j] = res[i]
print(data)
data.to_csv("diabetes_fixed_dataset.csv")

