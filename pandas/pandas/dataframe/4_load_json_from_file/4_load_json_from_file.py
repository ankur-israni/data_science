import pandas as pd;

# JSON = Python Dictionary
# JSON objects have the same format as Python dictionaries.
# Load the json file into a DataFrame
dataFrame = pd.read_json('data.json');

# Use to_string() to print the while DataFrame
print(dataFrame.to_string());
