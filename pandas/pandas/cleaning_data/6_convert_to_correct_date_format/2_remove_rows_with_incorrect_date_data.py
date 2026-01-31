# This example is not working because of this value in the Date field in 'data.csv' = "20201226"


import pandas as pd

df = pd.read_csv('data.csv')

# Convert all data to Date format
df['Date'] = pd.to_datetime(df['Date'])

# Drop data in 'Date' column which does not conform to Date type.
df.dropna(subset=['Date'], inplace = True)

print(df.to_string())
