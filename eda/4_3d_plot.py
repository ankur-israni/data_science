import pandas as pd
import plotly.express as plotly


iris_data_frame = pd.read_csv(r'./resources/iris.csv')

# TODO ; What is this for ?
plotly.data.iris()

# 3D plot, X-Axis = sepal_length, Y-Axis = sepal_width, Z-Axis = petal_width
# Plot 'species' column data using different colors.
# This will create a 3D plot and will open up in a browser window
# This will be an interactive plot - You will be able to move it around
# A legend for this also created
plot = plotly.scatter_3d(iris_data_frame, x='sepal_length', y='sepal_width', z='petal_width', color='species')

plot.show();