import numpy as np

array1 = np.array([1,2,9,4])
array2 = np.array([5,6,7,8])

# all()
# Logical AND
# if all elements in array1 < array2, then all=true, else all=false
all = np.all(array1 < array2)
print('all = ',all)


# any
# Logical OR
# if any element in array1 < array2, then or=true, else or=false
_or=np.any(array1 < array2)
print('_or = ',_or)



