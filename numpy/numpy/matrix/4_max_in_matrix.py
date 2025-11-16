import numpy as np

matrix = np.array([[1,2],
                   [3,4]])

# Find the max value by column, axis=0 means column
max_value_in_column=np.max(matrix,axis=0)
print('max_value_in_column = ',max_value_in_column)

# Find the max value by row, axis=1 means row
max_value_in_row=np.max(matrix,axis=1)
print('max_value_in_row = ',max_value_in_row)

