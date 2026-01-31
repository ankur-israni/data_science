'''
we cannot combine strings and numbers like this:
age = 36
print("age = "+age)

This will give an error since, the print() function is only allowed to print strings.
'''

# Wee can combine trings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is Ankur, and I am {}"
print("format() with single arguement = " + txt.format(age))


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print("format() with multiple arguements = "+myorder.format(quantity, itemno, price))

# You can use index numbers e.g. {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print("format() with index numbers = "+myorder.format(quantity, itemno, price))