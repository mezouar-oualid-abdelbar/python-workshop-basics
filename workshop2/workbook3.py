import pandas as pd

students = {
    'Name': ['Walid', 'Saber', 'Katib', 'Mohsen','Bashir'],
    'Subject': ['English', 'English', 'Math', 'Math' ,'Science'],
    'Score': [90, 30, 85, 70,90]
}

pdDataFrame= pd.DataFrame(students)

print(pdDataFrame)

print(pdDataFrame.head(3))

mathMask = pdDataFrame['Subject'] == 'Math'

print(pdDataFrame[mathMask])

mask2 = pdDataFrame['Score'] > 80

print(pdDataFrame[(mathMask) & (mask2)])

englishMask = pdDataFrame['Subject'] == 'Math'

print(pdDataFrame[(englishMask) & (mask2)])
