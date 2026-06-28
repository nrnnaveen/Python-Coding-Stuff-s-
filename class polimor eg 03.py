#creat a class employee and add property as name salary naxt creat a derived class manager
#and add property department and add function display in manager
#to print name salary dept
#you can use super key word

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.department=dep
    def display (self):
        print("NAME:",self.name)
        print("SALARY:",self.salary)
        print("DEPARTMENT:",self.department)
a= manager("EMC",20000,"CHEMICAL")
a.display()
