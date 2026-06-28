"""Get a input  of purchase amount from user and add 18% gst for it
 if the amount is greater than 10000 add 10 percent discount otherwise print total amount"""

Amount=int(input("Enter Purchase Amount:"))
Tax=(Amount*0.18)
Total=(Amount+Tax)
print("PURCHASE AMOUNT:",Amount)
print("GST:",Tax)
if Amount>10000 :
    Discount=(Total*0.10)
    Total=(Discount+Total)
    print("DISCOUNT:",Discount)
    print("TOTAL AMOUNT IS:",Total)
else:
    print("TOTAL AMOUNT IS:",Total)