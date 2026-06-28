""" You Are a Movie Ticket seller Get a input from user for age and profesonal if professonal and
age is student or >=65 eligible for discount other wise no  discount"""
Age = int(input("ENTER YOUR AGE:"))
Profeson= int(input("""YOUR PROFESON:
                   1.Working profeson
                   2.Student
                   3.Others
            Enter Your Choice No :-""") )

if Age >= 65 or Profeson == 2 :
    print("You Are Eligible For Discount")
else:
    print("Not Eligible For Discount")