import pandas as pd;

# By default, the dropna() method returns a new DataFrame, and will not change the original.
# origionalDataFrame = has errorneous data like Nulls. The entire row is dropped if it contains even one null/missing value
# resultDataFrame = no errorenous data, null rows are removed
origionalDataFrame = pd.read_csv('data.csv');
resultDataFrame = origionalDataFrame.dropna();

print("origional data frame : ");
print(origionalDataFrame);

print();
print("result data frame: ");
print(resultDataFrame);