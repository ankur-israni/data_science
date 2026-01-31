import pandas as pd;

# The dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
dataFrame = pd.read_csv('data.csv');
dataFrame.dropna(inplace=True);

print("Dataframe without errorenous data : ");
print(dataFrame);

