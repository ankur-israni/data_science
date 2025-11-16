import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

iris_data_frame = pd.read_csv(r'./resources/iris.csv')

sb.set_style("whitegrid")
sb.pairplot(iris_data_frame, hue="species", height=10)
plt.show()

