import numpy as np

array1 = np.array([1,2,9,4])
array2 = np.array([5,6,7,8])

# all()
# Logical AND
# if all elements in array1 < array2, then all=true, else all=false
# np.all(array1 < array2) means that are all elements in array 1 less than corresponding elements in array2. 
# Here, 9 is not less than 7, so all=false
all:bool = np.all(array1 < array2)
print('all = ',all)


# any
# Logical OR
# if any element in array1 < array2, then or=true, else or=false
# np.any(array1 < array2) means that is there any element in array1 less than corresponding element in array2.
_or:bool=np.any(array1 < array2)
print('_or = ',_or)



