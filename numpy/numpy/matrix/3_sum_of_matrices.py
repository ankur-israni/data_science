import numpy as np


matrix = np.array([[1,2],[3,4]])

# Calculate the sum of column elements
# axis = 0, means do the specified operation(here 'sum') on the column elements
# [1] + [3] = [4]
# [2] + [4] = [6]
# Output = [4,6]
sum_of_column_elements = np.sum(matrix,axis=0)
print("sum_of_column_elements = ",sum_of_column_elements)


# Calculate the sum of row elements
# axis = 1, means do the specified operation(here 'sum') on the row elements
# [1] + [2] = [3]
# [3] + [4] = [7]
# Output = [3,7]
sum_of_row_elements = np.sum(matrix,axis=1)
print("sum_of_row_elements = ",sum_of_row_elements)
