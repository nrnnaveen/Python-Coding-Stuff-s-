class teacher:
    def __init__(self,nam,reg):
        self.name=nam
        self.regno=reg
    def display(self):
        print("Name:",self.name)
        print("Reg No:",self.regno)
t1=teacher("priya","1234")
t2=teacher("swetha","4321")
t1.display()
t2.display()
