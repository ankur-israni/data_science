import pandas as pd;

# Info about the data
# Shows nulls, not-nulls, datatypes, header-names, memory usage, no of rows and columns, etc
dataFrame = pd.read_csv("data.csv");
print(dataFrame.info());