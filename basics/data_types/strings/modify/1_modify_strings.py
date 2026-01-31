# To upper case
str = "Hello, World!"
print("str.upper() = " + str.upper())

# To lower case
print("str.lower() = " + str.lower())

# Remove whitespace - will remove leading and trailing spaces
str2 = " Hello, World! "
print("str2.strip() = "+str2.strip())  # returns "Hello, World!"

# Replace string with another string
print("str.replace() = "+str.replace("H", "J"))

# Split string
# The split() method splits the string into substrings if it finds instances of the separator
split_strings = str.split(",") # Returns ['Hello', ' World!']
print("split strings = ")
print(*split_strings)
