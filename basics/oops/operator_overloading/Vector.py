# Operator overloading in python is done by defining special methods in a class.
# These special methods have double underscores at the beginning and end of their names.
# For example, to overload the '+' operator, we define the '__add__' method.
# Another example is the '-' operator, which can be overloaded by defining the '__sub__' method.


class Vector:

    # Constructor
    # Constructor has to be called '__init(self,...)__'
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Overriding str function.
    # This is like overriding the toString() method from Object class in Java
    # This method has to be called '__str__(self)'
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    # Overriding add function - whenever the plus operator in 'v1 + v2' is evaluated, this add() function will be called.
    # Here the plus operator is overloaded
    # Having the '__add(self,other)__'  method means you are overriding the '+' operator
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b) # this will call the constructor(__init__), self.a = 2. other.a=5, self.b=10,other.b=-2

    # Overriding add function - whenever the minus operator in 'v1 - v2' is evaluated, this add() function will be called.
    # Here the minus operator is overloaded
    # Having the '__add(self,other)__'  method means you are overriding the '-' operator
    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

# Execute
v1 = Vector(2, 10)
v2 = Vector(5, -2)
# print("v1 = "+str(v1))
# print("v2 = "+str(v2))
print("v1 + v2 = "+ str(v1 + v2))
# print("v1 - v2 = "+ str(v1 - v2))