import pandas as pd;

dataFrame = pd.read_csv('data.csv');

# Calculate the MODE
# Mode is the value that appears most frequently
# mode = dataFrame['Calories'].mode()[0];
mode = dataFrame['Calories'].mode();
print("Mode : ", mode);

# Replace the erroneous/missing data with MODE
dataFrame["Calories"].fillna(mode, inplace=True);
# print("\n Erroneous data replaced with Mode in 'Calories' column: \n", dataFrame.to_string());
