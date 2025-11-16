
'''
The first character has index 0.
'''

str = "Hello, World!"

# Get the characters from position 2 to position 5 (not included)
sliced_from_2nd_character = str[2:5]
print("sliced_from_2nd_character = "+sliced_from_2nd_character)

# Slice from the start
# By leaving out the start index, the range will start at the first character
sliced_from_beginning = str[:5]
print("sliced_from_beginning = "+sliced_from_beginning)

# Slice to the End
# Get the characters from position 2, and all the way to the end
sliced_to_the_end = str[2:]
print("sliced_to_the_end = "+sliced_to_the_end)

# Negative Indexing
# Use negative indexes to start the slice from the end of the string
negative_indexing = str[-5:-2]
print("negative_indexing = "+negative_indexing)