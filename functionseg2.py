# find pass or fail with user input using def
def findpassorfail(b):
    if(b<35):
        print("fail")
    elif(b>100):
        print("invalid input try again")
    elif(b>=35):
        print("pass")

a=int(input("ENTER YOUR MARK ?/100:"))
findpassorfail(a)
