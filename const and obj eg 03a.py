#creat clas calcu and add a,b varibles and func (add/sub/mul/div)
#to use init or consrector
class calculator:
    def __init__(self,a,b):
        self.m=a
        self.n=b
    def add(self):
        print("Answer is:",self.m+self.n)
    def sub(self):
        print("Answer is:",self.m-self.n)
    def mul(self):
        print("Answer is:",self.m*self.n)
    def div(self):
        print("Answer is",self.m/self.n)
cal=calculator(40,20)
cal.add()
cal.sub()
cal.mul()
cal.div()
