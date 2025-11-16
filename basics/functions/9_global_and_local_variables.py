total = 0;  # This is global variable.

# Function definition
def sum(arg1, arg2):
    total = arg1 + arg2;  # Here total is local variable.
    print("Local variable : total : ", total)
    return total;


# Execute
sum(10, 20);
print("Global variable : total : ", total)
