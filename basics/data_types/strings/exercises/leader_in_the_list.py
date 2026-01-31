# Find the leader in a list
# A number is a leader if all the numbers to the right side of a number are lesser that the number.

lst = [1,15,-1,4,9,5]

for i in range(len(lst)):
    flag = True
    for j in range(i+1,(len(lst))):
        if(lst[i]<lst[j]):
            flag = False
            break

    if(flag==True):
        print(list[i],"is a leader")
