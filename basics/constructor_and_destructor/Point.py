#Definition
class Point:
   # __init__ is the constructor method, gets called only once when the class is being instantiated
   def __init__( self, x=0, y=0):
      print("constructor")
      self.x = x
      self.y = y

   # __del__ is the constructor_and_destructor method, gets called only once when the class is being deallocated memory
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destructor")

#Execution 
pt1 = Point()
pt2 = pt1
pt3 = pt1

# prints the ids of the objects - they are all the same, since reference is being assigned 
print(id(pt1), id(pt2), id(pt3))

# delete instances of Point class
del pt1
del pt2
del pt3
