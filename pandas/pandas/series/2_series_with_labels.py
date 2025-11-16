import pandas as pd;

# Create Series from a  list with labels and print it.
data = [1,7,2];
mySeries = pd.Series(data,index = ["x","y","z"]);
print("series with labels:");
print(mySeries);


# Retrieve an item from the series by calling using its label
print();
print("Element 'y from the series = "+str(mySeries["y"]));