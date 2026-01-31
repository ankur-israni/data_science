import pandas as pd;


dataFrame = pd.read_csv('data.csv');

# Calculate the MEAN
# Mean = the average value (the sum of all values divided by number of values).
mean = dataFrame['Calories'].mean();
print("Mean : ",mean);

# Replace the erroneous/missing data in the column 'Calories' with MEAN
dataFrame["Calories"].fillna(mean, inplace=True);
# print("\n Erroneous data replaced with Mean in 'Calories' column: \n",dataFrame.to_string());
