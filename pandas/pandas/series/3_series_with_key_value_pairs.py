import pandas as pd;

# Create a series from a dictionary with Key Value pairs
calories = {"day1": 420, "day2": 300, "day3": 390};
myFullSeries = pd.Series(calories);
print("Series with key value pairs (all days): ");
print("myFullSeries: ",myFullSeries);
print();

# Create a Series using only data from 'day1' and 'day2'
mySeriesOfSelectedDays = pd.Series(calories, index=["day1", "day2"]);
print("Series with key value pairs (selected days): ");
print(mySeriesOfSelectedDays);


