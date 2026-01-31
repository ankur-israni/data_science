import pandas as pd;

dataFrame = pd.read_csv('data.csv');

# Replace incorrect data (i.e. 450) at ROW = 7(# = 8), COLUMN = 'Duration' with CORRECT_DATA = 33
# Note that First Row = Row 0
# This will replace in the dataframe itself, not in the origional csv file.
# Here 7 = Row Number, Duration = Column Name
dataFrame.loc[7,'Duration'] = 33;

print('Dataframe with Row 7, Column = Duration replaced with correct data: ')
print(dataFrame.to_string());