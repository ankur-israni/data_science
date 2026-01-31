# Count how many times (1) occurs using for loop
lst = [1,2,1,8,9,1]

count = 0
for i in lst:
    if(i==1):
        count=count+1

print(count)

#Built in way of counting occurence of element in a list
print(lst.count(1));