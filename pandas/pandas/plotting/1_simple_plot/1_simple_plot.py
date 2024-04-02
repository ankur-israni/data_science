import pandas as pd
import matplotlib.pyplot as plt
import sys

# Create a simple plot
# The 'plot()' method will ignore non-numeric data in the data file
df = pd.read_csv('1_simple_plot/data.csv')

df.plot();

plt.show();

