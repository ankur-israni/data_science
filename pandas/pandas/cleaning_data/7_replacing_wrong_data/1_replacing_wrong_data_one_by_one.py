import pandas as pd;

dataFrame = pd.read_csv('data.csv');

# Replace incorrect data at ROW = 7, COLUMN = 'Duration' with CORRECT_DATA = 45
# Note that First Row = Row 0
dataFrame.loc[7,'Duration'] = 45;

print('Dataframe with Row 7, Column = Duration replaced with correct data: ',dataFrame.to_string());