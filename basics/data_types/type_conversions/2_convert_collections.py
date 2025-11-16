# convert a set to a list
def list_to_set():
    mylist = [1, 2, 3, 3, 4, 6, 7, 7]
    myset = set(mylist)
    print('converted list to set (duplicates will be deleted)= ', myset)

# Convert set to tuple
def set_to_tuple():
    myset = {1, 2, 3}
    mytuple = tuple(myset)
    print("converted set to tuple = ", mytuple)

# Convert list to set
def list_to_set():
    mylist = [1, 2, 3, 4]
    myset = set(mylist)
    print("converted list to set = ", myset)

# Convert list to tuple
def list_to_tuple():
    mylist = [4, 5, 6, 7, 8, 9]
    mytuple = tuple(mylist)
    print("converted list to tuple = ", mytuple)

# Execution
list_to_set()

set_to_tuple()

list_to_set()

list_to_tuple()


