class Employee:
    # class variable - similar to java's static variable - accessible with class name
    empCount = 0

    # constructor
    def __init__(self, name, salary):
        self.name = name; # instance variable
        self.salary = salary; # instance variable
        Employee.empCount += 1;

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount);

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary);


# Execute
emp1 = Employee("Zara", 2000) # emp1, emp2 are objects of Employee class
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employees:  %d" % Employee.empCount)