# Here, 'mylist' is passed as a reference.mylist
# i.e. the memory address of the list is passed to the function, when the list is updated by the 'updateList' function,
# the changes are reflected outside the function as well.

def updateList( mylist ):
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Execute function
mylist = [10,20,30];
updateList(mylist);
print("Values outside the function: ", mylist)