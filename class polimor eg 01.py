class person():
    def __init__(self,name,):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print("Name:",self.name)
        print("Grade:",self.grade)


a=student("emc","a+")
a.display()
