# Max occurences of elements with their count.
lst =['rest1','rest2','rest3','rest4','rest1','rest5','rest2','rest2']

dictionary={}
print(type(dictionary));
for element in lst:
   if (dictionary.get(element) != None):
    dictionary[element]=dictionary[element]+1
   else:
    dictionary[element]=1



print(dictionary)
type(dictionary)


# Which key has the highest value ?
highestValue = 0;
for k,v in dictionary.items():
    if(v > highestValue):
        highestKey = k;
        highestValue = v;

print("highestKey = ",highestKey)
print("highestValue = ",highestValue)