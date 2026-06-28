"""
✅ Problem Statement
Given a positive integer n, perform the following actions:

If n is odd, print Weird

If n is even and in the inclusive range 2 to 5, print Not Weird

If n is even and in the inclusive range 6 to 20, print Weird

If n is even and greater than 20, print Not Weird

✅ Input Format
A single line containing a positive integer n.

✅ Constraints
1 <= n <= 100
"""

n=int(input("Enter No(n):"))
if(1<=n<=100):
    if(n%2==1):
        print("Weird")
    elif(n%2==0 and 2<=n<=5):
        print("Not Weird")
    elif(n%2==0 and 6<=n<=20):
        print("Weird")
    elif(n%2==0 and n>20):
        print("Not Weird")
else:
    print("INVALID INPUT")

