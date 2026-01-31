# Note: This example will throw an error, since we are trying to print a deleted property
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

# Execution
p1 = Person("John", 36)
del p1.age
print(p1.age)
