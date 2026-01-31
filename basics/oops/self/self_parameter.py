
# 'self' can be called something else too e.g. 'abc', etc
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Here 'xyz' is 'self'
  def myfunc(xyz):
    print("Hello my name is " + xyz.name)

# Execution
p1 = Person("John", 36)
p1.myfunc()