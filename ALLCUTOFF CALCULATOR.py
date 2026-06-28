print("WELCOME TO CUTOFF CALCULATOR 2026")

print("""
which cutoff do you want to calculate:
        1. TNEA(ENGINEERING)
        2. TNAU(AGRICULTURE)
        3. TNDALU(LAW)
        4. TNGASA(ARTS & SCIENCE)
        5. TNMEDICAL SELECTION (PARAMEDICAL)
        6. TANUVAS (VEDNERY)
        
""")
N=int(input("PLEASE ENTER YOUR CHOICE NO:"))

if(N==1):
    print("WELCOME TO TNEA 2026 CUTOFF CALCULATOR")
    phy=int(input("ENTER PHYSICS SCORE /100:"))
    che=int(input("ENTER CHEMISTRY SCORE /100:"))
    math=int(input("ENTER MATHS SCORE /100:"))
    phy_che=((phy/2)+(che/2))
    print("CONGRATS YOUR ENGINEERING CUTOFF IS:",(phy_che)+(math))

    
elif(N==2):
    print("WELCOME TO TNAU 2026 CUTOFF CALCULATOR")
    phy=int(input("ENTER PHYSICS SCORE /100:"))
    che=int(input("ENTER CHEMISTRY SCORE /100:"))
    math=int(input("ENTER MATHS SCORE /100:"))
    bio=int(input("ENTER YOUR BIOLOGY SCORE /100:"))
    phy_che=((phy/2)+(che/2)+(math/2)+(bio/2))
    print("CONGRATS YOUR AGRICULTURE CUTOFF IS:",(phy_che))

elif(N==3):
    print("WELCOME TO TNDALU 2026 CUTOFF CALCULATOR")
    phy=int(input("ENTER MAIN SUB 1 SCORE /100:"))
    che=int(input("ENTER MAIN SUB 2 SCORE /100:"))
    math=int(input("ENTER MAIN SUB 3 SCORE /100:"))
    bio=int(input("ENTER YOUR MAIN SUB 4 SCORE /100:"))
    phy_che=((phy/2)+(che/2)+(math/2)+(bio/2))
    print("CONGRATS YOUR LAW CUTOFF IS:",(phy_che))

elif(N==4):
    print("WELCOME TO TNGASA 2026 CUTOFF CALCULATOR")
    phy=int(input("ENTER MAIN SUB 1 SCORE /100:"))
    che=int(input("ENTER MAIN SUB 2 SCORE /100:"))
    math=int(input("ENTER MAIN SUB 3 SCORE /100:"))
    bio=int(input("ENTER YOUR MAIN SUB 4 SCORE /100:"))
    phy_che=((phy/2)+(che/2)+(math/2)+(bio/2))
    print("CONGRATS YOUR ARTS & SCIENCE CUTOFF IS:",(phy_che))
          
elif(N==5):
    print("WELCOME TO TN MEDICAL(PARA) 2025 CUTOFF CALCULATOR")
    phy=int(input("ENTER MAIN SUB 1 SCORE /100:"))
    che=int(input("ENTER MAIN SUB 2 SCORE /100:"))
    math=int(input("ENTER MAIN SUB 3 SCORE /100:"))
    bio=int(input("ENTER YOUR MAIN SUB 4 SCORE /100:"))
    phy_che=((phy/2)+(che/2)+(math/2)+(bio/2))
    print("CONGRATS YOUR PARAMEDICAL CUTOFF IS:",(phy_che))

          

elif(N==6):
    print("WELCOME TO TANUVAS 2026 CUTOFF CALCULATOR")
    phy=int(input("ENTER PHYSICS SCORE /100:"))
    che=int(input("ENTER CHEMISTRY SCORE /100:"))
    math=int(input("ENTER BIOLOGY SCORE /100:"))
    phy_che=((phy/2)+(che/2))
    print("CONGRATS YOUR VEDNERY CUTOFF IS:",(phy_che)+(math))

else:
    print("INVALID INPUT TRY AGAIN")

""" Iam Developed this  using conditional statements  - Naveen """

    

