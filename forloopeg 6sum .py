a=[]
print("ENTER 10 NO:")
for i in range(10):
    num=int(input("ENTER NO:" +str(i+1)))
    a.append(num)
print("A is:",a)
sum=0
for i in a:
    sum=sum+i
print("SUM IS:",sum)
print("AVERAGE IS:",sum/10)
