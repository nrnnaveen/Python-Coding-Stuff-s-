"""a=int(input("enter item no:"))
b=int(input("enter quenty:"))
c=float(input("entder price:"))
d="i want to pay {2} dollers for {1} pices of item {0}"
print(d.format(a,b,c))"""
"""a=200
b=2
c=a/b
print(c)
"""
"""
import mymodule
a=mymodule.person2["dep"]
print(a)
"""
"""
import mymodule as am

b= am.person1["age"]
print(b)
"""
"""
import platform

x = platform.system()
print(x) 
"""
"""
import platform

x = dir(platform)
print(x) 
"""
"""
import datetime
n=datetime.datetime.now()
print(n)
"""
"""
print("WELCOME TO NRN CALCULATOR")
print(""" #ENTER YOUR CHOICE :-
           # A.ADD(+)
            #B.SUB(-)
            #C.MUL(×)
            #D.DIV(÷)
""")

n=str(input(":"))


def add():
    a=int(input("ENTER NO 1:"))
    b=int(input("ENTER NO 2:"))
    print("ANSWER IS:",a+b)
    
def sub():
    a=int(input("ENTER NO 1:"))
    b=int(input("ENTER NO 2:"))
    print("ANSWER IS:",a-b)
    
def mul():
    a=int(input("ENTER NO 1:"))
    b=int(input("ENTER NO 2:"))
    print("ANSWER IS:",a*b)
    
def div():
    a=int(input("ENTER NO 1:"))
    b=int(input("ENTER NO 2:"))
    print("ANSWER IS:",a/b)

A=add()
B=sub()
C=mul()
D=div()
"""


