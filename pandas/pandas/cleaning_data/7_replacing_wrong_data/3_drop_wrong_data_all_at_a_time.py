import pandas as pd

# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analysis.
dataFrame = pd.read_csv('data.csv')

# Delete wrong data from the DataFrame.
# Here wrong data is where Duration > 120
for x in dataFrame.index:
  if dataFrame.loc[x, "Duration"] > 120:
    dataFrame.drop(x, inplace = True)



print('Wrong data deleted, Wrong data is where Duration > 120: \n',dataFrame.to_string());