n=int(input("ENTER A NUMBER:"))
sum=0
print("the first",(n),"natural numbers are")
for i in range(1,n+1):
    print(i,end='')
    sum=sum+i
print("sum of first ",(n), "natural number is:", sum)
