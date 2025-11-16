import pandas as pd

# Calculate corelation coeffecient for simple data - also called "Pierson's r"
print();
dataFrame = pd.read_csv('simple_data.csv')
print("Corelation coffecient or Pierson's r (Simple data) : ")
print(dataFrame.corr())

# Calculate corelation coeffecient for a lot of complex data - also called "Pierson's r"
dataFrame = pd.read_csv('complex_data.csv');
print("Corelation coffecient or Pierson's r (Complex data) : ");
print(dataFrame.corr());


