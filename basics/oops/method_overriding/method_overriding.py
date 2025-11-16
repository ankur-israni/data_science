class Parent:        # define parent class
   def myMethod(self):
      print('Calling parent method')

class Child(Parent):
   pass;

   #If you uncomment the below, it will call child.myMethod() instead of parent.myMethod()
   # def myMethod(self):
   #    print('Calling child method')


# Execute
child = Child();
child.myMethod()         # child calls overridden method