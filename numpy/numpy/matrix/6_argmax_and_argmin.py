import numpy as np

twoDimensionArray = np.array([[1, 2, 3], [4, 5, 6]]);

# argmax > row
# Find the index of the highest element,
# highest elements: 3,6
# at Index = 2,2
# axis=1 (row)
argmax_row = np.argmax(twoDimensionArray, axis=1)
print('argmax_row = ',argmax_row);

# argmax > col
# Find the index of the highest element,
# highest elements: 4,5,6
# at Index = 1,1,1
# axis=0 (column)
argmax_column = np.argmax(twoDimensionArray, axis=0)
print('argmax_column = ',argmax_column);

# argmin > row
# Find the index of the lowest element,
# lowest elements: 1,4
# at index 0,0
# axis=1 (row)
argmin_row = np.argmin(twoDimensionArray, axis=1)
print('argmin_row = ',argmin_row);

# argmin > column
# Find the index of the lowest element,
# lowest elements: 1,2,3
# at index 0,0,0
# axis=1 (row)
argmin_column = np.argmin(twoDimensionArray, axis=0)
print('argmin_column = ',argmin_column);