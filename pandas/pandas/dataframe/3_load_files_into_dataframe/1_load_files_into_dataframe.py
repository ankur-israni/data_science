import pandas as pd;



# Set Max returned rows as 9999
pd.options.display.max_rows = 9999;

# Check the max rows values
print("Max rows that can be read from the CSV file: ");
print(pd.options.display.max_rows)

# Read from a CSV file.

# Place the CSV file in the directory - pandas/3_load_files_into_dataframe
print();
dataFrame = pd.read_csv('3_load_files_into_dataframe/data1.csv');

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows when using - print(dataFrame);
# use to_string() to print the entire DataFrame - print(dataFrame.to_string());
print(dataFrame.to_string());