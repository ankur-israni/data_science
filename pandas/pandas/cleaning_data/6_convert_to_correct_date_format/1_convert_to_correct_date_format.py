# This example is not working because of this value in the Date field in 'data.csv' = "20201226"

import pandas as pd;

dataFrame = pd.read_csv('data.csv');

# Convert data to Date format in the column called 'Date'
dataFrame['Date'] = pd.to_datetime(dataFrame['Date']);
print(dataFrame.to_string());

