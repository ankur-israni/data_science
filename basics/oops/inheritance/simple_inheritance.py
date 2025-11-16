# Note: Both the parent and the child classes should be in the same python file.
# If you move the Parent and Child classes to different python files, then isSubClass does not work.

class Parent:
  parentAttr = 100

  def __init__(self):
    print("Calling parent constructor")

  def parentMethod(self):
    print('Calling parent method')

  def setAttr(self, attr):
    Parent.parentAttr = attr

  def getAttr(self):
    print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # This syntax denotes inheritance
  def __init__(self):
    print("Calling child constructor")

  def childMethod(self):
    print('Calling child method')

# Execute
child_object = Child()  # instance of child
child_object.childMethod()  # child calls its method
child_object.parentMethod()  # calls parent's method
child_object.setAttr(200)  # again call parent's method
child_object.getAttr()  # again call parent's method

# issubclass
issubclass = issubclass(Child,Parent)
print("issubclass = "+str(issubclass))


# isinstance - isinstance is a built in function in Python
isinstance1 = isinstance(child_object, Parent)
print("isinstance(child_object, Parent) = "+str(isinstance1))

isinstance2 = isinstance(child_object, Child)
print("isinstance(child_object, Child) = "+str(isinstance2))