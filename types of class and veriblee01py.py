class laptop:
    charge="b-type"

    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print("Price:",self.price)

    @classmethod #to define or
    def changecharge(cl):
        cl.charge="c-type"
        print("charger type changed to:",cl.charge)
    @staticmethod # to define or 
    def info():
        print("THIS IS : LAPTOP CLASS")

hp=laptop()
hp.setprice(10000)
hp.getprice()

laptop.changecharge() #enter these ()
hp.info()#enter these()
