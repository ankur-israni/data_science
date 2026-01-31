import pandas as pd;


dataFrame = pd.read_csv('data.csv');

# Calculate the MEDIAN
# Median = the value in the middle, after you have sorted all values ascending.
median = dataFrame['Calories'].median();
print("Median : ",median);

# Replace the erroneous/missing data with MEAN
dataFrame["Calories"].fillna(median, inplace=True);
# print("\n Erroneous data replaced with Median in 'Calories' column: \n",dataFrame.to_string());
