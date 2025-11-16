import pandas as pd;

# For Column 'x' only, replace errorneous values with the value '999'
dataFrame = pd.read_csv('data.csv');
dataFrame['x'].fillna(999,inplace=True);
print('Result dataFrame : \n',dataFrame);

