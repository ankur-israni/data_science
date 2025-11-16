import pandas as pd;

# The tail() method returns the headers and a specified number of rows, starting from the bottom.
# Read the first 10 rows using tail(10)
print("Last 10 rows: ");
dataFrame = pd.read_csv('data.csv');
dataFrameOfLast10Rows=dataFrame.tail(10);
print(dataFrameOfLast10Rows);


# If you use the tail() without any parameters, it will read last 5 rows by default
print();
print("Last 5 rows :")
dataFrameOfLast5Rows=dataFrame.tail();
print(dataFrameOfLast5Rows);
