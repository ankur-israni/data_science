# Any variable that starts with __ is hidden from outside the class.
# It cannot be accessed directly, but can be accessed through public methods of the class.
# This is called data hiding in OOPs.
# Similar to private variables in Java.


class Counter:
    __secretCount = 0;

    def count(self):
        self.__secretCount += 1

# Execution
obj = Counter();
obj.count();
obj.count();

# This will throw an error because 'secretCount' is hidden and is only allowed inside the class
#  print(obj.__secretCount);

# This will work fine
print("secret count = ",obj._Counter__secretCount)
