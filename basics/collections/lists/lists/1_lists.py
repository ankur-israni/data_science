# List 
# Ordered collection, 
# Mutable (Elements can be changed, added, deleted, updated)
# Indexable (By Position)
# Duplicates allowed



# Create a list and print
myList = ["apple","cherry","banana","cheeku","pineapple","watermelon"];
print(myList);

# Length of list
print();
lenghtOfList = len(myList);
print("Length of list = " + str(lenghtOfList)); #print() function can only print 'string' values, so converting 'int' to 'string'

# First element of list
print();
firstElementOfList = myList[0];
print("First Element = "+firstElementOfList);

# Second thru Fourth elements of list i.e. 0,1,2,3. Element no '4' is not included
print();
secondThruFourthElements = myList[1:4];
print("Second thru Fourth elements = ");
print(secondThruFourthElements);


# All elements after 2nd element
print();
elementsAfterSecondThruLast = myList[2:];
print("Elements second thru last = ");
print(elementsAfterSecondThruLast);

