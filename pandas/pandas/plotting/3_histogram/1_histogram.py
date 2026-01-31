import pandas as pd;
import matplotlib.pyplot as plt;

# Create a histogram
# The 'plot()' method will ignore non-numeric data in the data file
# The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.
dataFrame = pd.read_csv("data.csv");
dataFrame.plot(kind='hist');
plt.show();