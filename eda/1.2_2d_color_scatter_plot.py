import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

iris_data_frame = pd.read_csv(r'./resources/iris.csv')

# Colorful 2D scatter plot using SEABORN
# 'whitegrid' add the white graph like grid in the background of the plot
sb.set_style("whitegrid");

# Create a 2D Scatter Plot between 'X Axis = sepal_width' and 'Y axis = sepal_width'
# Plot data from 'Species' column on this plot
# Add the legend using 'add_legend()' function
# hue = species means color code the value of species on the plot - orange, green, etc
sb.FacetGrid(iris_data_frame, hue="species").map(plt.scatter, "sepal_width", "sepal_length").add_legend()

plt.show()