salary=int(input("ENTER YOUR SALARY:"))
age=int(input("ENTER YOUR AGE :"))
if (salary>=20000 or age<=25):
    n=int(input("ENTER LOAN AMMOUNT:"))
    if(n<=50000):
        print("YOU ARE ELIGIBLE TO GRT LOAN")
    elif(n>50000):
        print("MAXIMUM OF LOAN AMMOUNT IS 50,000")
else:
    print("YOU ARE NOT ELIGIBLE TO GET LOAN")
