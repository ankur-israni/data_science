import pandas as pd;

iris_data_frame = pd.read_csv(r'./resources/iris.csv');

# Get the total count of different type of 'species' in the species column
species_count = iris_data_frame['species'].value_counts();
print("Total count of different type of 'species' in the species column : ",species_count);