# Definition
def printinfo(name, age=35):
    print("Name: ", name)
    print("Age ", age)
    return;


# Execution
printinfo(age=50, name="miki")
printinfo(name="miki") #Here age is not passed, default value will be used
