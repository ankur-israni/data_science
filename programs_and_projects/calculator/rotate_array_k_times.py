# Rotate and array 'count' times
# last element goes to 1st place of the array 'count' times


lst = [1,2,4,5,6,7,8]
count = 2 # Rotate this array 2 times
#output = [7,8,1,2,3,4,5,6]

'''
counter = 1;
i = 0
for element in lst:
    if(counter > count):
        break;
    else:
        element[i+1] = element[i]
        counter = counter + 1

print(lst);
'''


# Sandeeps solution
for i in range(count):
   a = lst.pop()
   lst.insert(0,a)
print(lst)

