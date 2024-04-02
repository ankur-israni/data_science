import numpy as np


matrix = np.array([[1,2],[3,4]])

# Calculate the sum of column elements
# axis = 0, means column elements
sum_of_column_elements = np.sum(matrix,axis=0)
print("sum_of_column_elements = ",sum_of_column_elements)


# Calculate the sum of row elements
# axis = 1, means row elements
sum_of_row_elements = np.sum(matrix,axis=1)
print("sum_of_row_elements = ",sum_of_row_elements)
