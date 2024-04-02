import seaborn as sb;
import matplotlib.pyplot as plt;
import pandas as pd;

iris_data_frame = pd.read_csv(r'./resources/iris.csv');




# 2D Scatter plot using MATPLOTLIB
iris_data_frame.plot(kind='scatter', x='sepal_length', y='sepal_width')
plt.show();

