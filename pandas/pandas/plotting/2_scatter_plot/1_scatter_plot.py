import pandas as pd;
import matplotlib.pyplot as plt;

# Scatter plot
# Note that in the 'plot()' function below, the x='Duration' and y='Calories' should match the column names EXACTLY in 'data.csv'
# The 'plot()' method will ignore non-numeric data in the data file
dataFrame = pd.read_csv("data.csv");
dataFrame.plot(kind='scatter', x='Duration', y='Calories');
plt.show();