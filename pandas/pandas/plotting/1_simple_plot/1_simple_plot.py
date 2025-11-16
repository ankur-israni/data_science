import pandas as pd
import matplotlib.pyplot as plt


# Create a simple plot
# The 'plot()' method will ignore non-numeric data in the data file
df = pd.read_csv('data.csv')

df.plot();

plt.show();
