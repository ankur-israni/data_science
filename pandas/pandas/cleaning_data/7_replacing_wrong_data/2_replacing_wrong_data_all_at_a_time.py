import pandas as pd

dataFrame = pd.read_csv('data.csv')

# Replace data in 'Duration' column, where it is greater than 120, to be 120
for x in dataFrame.index:
  if dataFrame.loc[x, "Duration"] > 120:
    dataFrame.loc[x, "Duration"] = 120

print('Data with Duration > 120 replaced with Duration = 120: ')
print(dataFrame.to_string())