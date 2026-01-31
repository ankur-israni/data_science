import pandas as pd;

# Create and print a 'Series' from a list
data = [3,7,2];
mySeries = pd.Series(data);
print("mySeries:");
print(mySeries);


# Print the first element in the series
# First value has index 0.
print();
print("First elment of series : "+str(mySeries[0]));


