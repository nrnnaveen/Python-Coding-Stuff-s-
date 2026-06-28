class student:
    def __init__(self):
        self.name=""
        self.regno=0
    def display(self):
        print("Name:",self.name)
        print("Reg No:",self.regno)
s1=student()
s2=student()
s1.name="EMC"
s1.regno=1275417
s2.name="CME"
s2.regno=1275418


s1.display()
s2.display()
