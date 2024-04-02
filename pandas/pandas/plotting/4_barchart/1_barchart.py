import pandas as pd;
import matplotlib.pyplot as plt;

# Create a histogram
# The 'plot()' method will ignore non-numeric data in the data file
dataFrame = pd.read_csv("data.csv");
dataFrame.plot(kind='bar');
plt.show();