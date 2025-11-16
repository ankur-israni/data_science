# Find missing no from the list
# max = max no in the list

lst = [1, 2, 3, 3, 4, 6, 7, 7]
max = 7
# output: missing number = 5



# Convert to set - This will (1) delete duplicates and (2) will put in sorted order
# myset = {x for x in lst}
myset = set(lst)

# print(myset)

index = 1
for i in range(1, max):
    if i not in myset:
        print("missing element = ", i)
