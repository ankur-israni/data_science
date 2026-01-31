#  - The parameter mylist is local to the function changeme. Changing mylist within the function does not affect mylist(from outside the function).

# Function definition is here
def changeme(mylist):
   mylist = [1,2,3,4]; # This would assign new reference in mylist. mylist(outside) would remain unchanged and be stored in a different memory location.
   print("Values inside the function: ", mylist)
   return

# Execute function
mylist = [10,20,30];
changeme(mylist);
print("Values outside the function: ", mylist)