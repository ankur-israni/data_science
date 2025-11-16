import pandas as pd;


# Create and print simple DataFrame
# Here 'cars' and 'ratings' are like two Series (or two columns)
# data (which is a DataFrame) is like the whole table with all columns and rows.
data = {
  'cars': ["BMW", "Volvo", "Ford"],
  'ratings': [3, 7, 2]
}

# Pandas DataFrame
myDataFrame = pd.DataFrame(data)
print("DataFrame:");
print(myDataFrame)


# Pandas can use the 'loc' attribute to return one or more specified row(s).
# This returns a Pandas Series
print();
rowZero = myDataFrame.loc[0];
print("rowZero = ");
print(rowZero);

# When using [], the result is a Pandas DataFrame
# Note the usage of Double Square Brackets in 'loc[[0,1]]'
print();
rowZeroAndOne = myDataFrame.loc[[0,1]];
print("rowZeroAndOne: ");
print(rowZeroAndOne);