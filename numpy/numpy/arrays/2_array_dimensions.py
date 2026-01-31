import numpy as np;

def printNumpyArrayDetails(name_of_array,array):
    print("-------------------------------------")
    print();
    print("arrayname = ",name_of_array)
    print("Shape / dimensions of array:",array.shape)
    print("dimensions of array",array.ndim)
    print("\nThe array: ",array)
    print("-------------------------------------")

# Create 0-Dimension array
# 0-D arrays, or SCALARS, are the elements in an array. Each value in an array is a 0-D array
zeroDimensionArray =  np.array(42);

# Create 1-Dimension array
# An array that has 0-D arrays as its elements is called UNI-DIMENSIONAL or 1-D array.
oneDimensionArray =  np.array([1,2,3,4,5]);


# Create 2-Dimension array
# An array that has 1-D arrays as its elements is called a 2-D array.
twoDimensionArray = np.array([[1, 2, 3], [4, 5, 6]]);



# Create 3-Dimension array
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
threeDimensionArray = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 12, 13], [14, 15, 16]]]);


# Higher dimension arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.
# In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector,
# - the 3rd dim has 1 element that is the matrix with the vector,
# - the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
higherDimensionArray = np.array([1, 2, 3, 4], ndmin=5)



# Check the dimensions of the arrays
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
# print("\nNumber of dimensions for the array zeroDimensionArray = ",zeroDimensionArray.ndim);
# print("\nNumber of dimensions for the array oneDimensionArray = ",oneDimensionArray.ndim);
# print("\nNumber of dimensions for the array twoDimensionArray = ",twoDimensionArray.ndim);
# print("\nNumber of dimensions for the array threeDimensionArray = ",threeDimensionArray.ndim);
# print("\nNumber of dimensions for the array higherDimensionArray = ",higherDimensionArray.ndim,);

printNumpyArrayDetails('zeroDimensionArray',zeroDimensionArray)
printNumpyArrayDetails('oneDimensionArray',oneDimensionArray)
printNumpyArrayDetails('twoDimensionArray',twoDimensionArray)
printNumpyArrayDetails('threeDimensionArray',threeDimensionArray)
printNumpyArrayDetails('higherDimensionArray',higherDimensionArray)



