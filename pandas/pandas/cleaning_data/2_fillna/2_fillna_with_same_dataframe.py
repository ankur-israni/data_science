import pandas as pd;

# The fillna(inplace = True) will NOT return a new DataFrame, but it will replace all rows containing NULL values from the original DataFrame.
# The errorneous values will be replaced with the value '999' in this example.
dataFrame = pd.read_csv('data.csv');
dataFrame.fillna(999,inplace=True);
print("\n Final dataFrame: \n",dataFrame);