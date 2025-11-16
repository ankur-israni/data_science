# Prerequisite: Install pandas library
# Terminal > pandas/pandas/analyzing_data/1_head> pip install pandas

#Running the script
# Terminal > pandas/pandas/analyzing_data/1_head> python3 1_head.py


import pandas as pd;

# The head() method returns the headers and a specified number of rows, starting from the top.
# Read the top 10 rows using head(10)
print("Top 10 rows: ");
dataFrame = pd.read_csv('data.csv');
dataFrameOfTop10Rows=dataFrame.head(10);
print(dataFrameOfTop10Rows);


# If you use the head() without any parameters, it will read Top 5 rows by default
print();
print("Top 5 rows :")
dataFrameOfTop5Rows=dataFrame.head();
print(dataFrameOfTop5Rows);
