class Employee:
    # class variable - similar to java's static variable - accessible with class name
    empCount = 0

    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary

# Execute
emp1 = Employee("Zara", 2000)

# hasattr() - built in function in Python
has_name = hasattr(emp1, 'name')  # Returns true if 'name' attribute exists
print("has_name = "+str(has_name));

# getattr() - built in function in Python
name = getattr(emp1, 'name')    # Returns value of 'name' attribute
print("name = "+name)

# setattr() - built in function in Python
setattr(emp1, 'salary', 1000)
salary = getattr(emp1,'salary')
print("salary = "+str(salary))

# delattr() - built in function in Python
delattr(emp1, 'name')
has_name = hasattr(emp1, 'name')  # Returns true if 'name' attribute exists
print("has_name = "+str(has_name));