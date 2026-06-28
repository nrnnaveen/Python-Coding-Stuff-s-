"""
### 🔢 **Conditionals & Loops**

4. Write a program to check if a number is even or odd.
5. Write a program to find the largest of three numbers.
6. Write a program to print numbers from 1 to 100 using a loop.
7. Write a program to print the multiplication table of a number.
8. Write a program to check if a number is prime.


"""
"""
#4
n=int(input("ENTER NO:"))
if(n%2==-0):
    print("EVEN")
else:
    print("ODD")
"""
"""
#5
a=int(input("ENTER NO 1:"))
b=int(input("ENTER NO 2:"))
c=int(input("ENTER NO 3:"))
if(a>b and a>c):
    print("ANSWER IS :",a)
elif(b>a and b>c):
    print("ANSWER IS:",b)
else:
    print("ANSWER IS:",c)
"""
"""
#6
for i in range (1,101):
    print(i,end=",")
"""
#7
n=int(input("ENTER MULTIPLICATION TABLE NO:"))
for i in range(1,17):
    print(i,"*",(n),"=",i*n,)
    
