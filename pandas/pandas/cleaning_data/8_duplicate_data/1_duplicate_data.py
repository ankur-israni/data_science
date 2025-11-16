import pandas as pd

dataFrame = pd.read_csv('data.csv')

# Check if data is duplicated for each row
print("Is Data Duplicated : ",dataFrame.duplicated());

# Remove duplicate data
print("\n Removing duplicate data: ");
dataFrame.drop_duplicates(inplace = True)

# Print the dataframe after removing duplicate data.
# Notice the duplicate row (Row #12) has been deleted
print("\n DataFrame after removing  duplicate data: ");
print(dataFrame.to_string())

