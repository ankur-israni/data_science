# Set =
# - Unordered collection (Order of elements in which they were inserted may not be preserved)
# - Mutable (can be changed, new elements be added or deleted or updated),
# - Duplicates - Does not allow duplicates
# - Not indexed - which means that you cannot do set[0] - this will give an error.

# Create a simple set
set = {1,2,3,4,5,5,5}
print("set = ",set)

# Set is not indexed i.e. the following statement will throw and exception
# print(set[0])