# Definition
def printinfo(arg1, *arg2 ):
   print("arg1 = "+str(arg1))
   for var in arg2:
      print("arg2 = "+str(var))
   return;

# Execution
printinfo(10) #arg1 = 10
printinfo(70,60,50) #arg1 = 70 arg2 = (60,50)