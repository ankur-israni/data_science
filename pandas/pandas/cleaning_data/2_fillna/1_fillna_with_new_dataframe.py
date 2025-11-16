import pandas as pd;

# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# origionalDataFrame = has errorneous data like Nulls
# resultDataFrame = no errorenous data, null values are replaced with 999   .
origionalDataFrame = pd.read_csv('data.csv');
resultDataFrame = origionalDataFrame.fillna(999);

print("Original DataFrame:\n", origionalDataFrame);
print();
print("Result DataFrame :\n",resultDataFrame);