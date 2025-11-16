# List comprehension - A concise element of creating a list

lst = [ 2,3,4,5]
op=[i**2 for i in lst]

print(op)


# For loop way
op2=[]
for i in lst:
    op2.append(i**2)

print(op2)