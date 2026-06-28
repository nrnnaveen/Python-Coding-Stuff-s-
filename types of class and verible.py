class phone:
    charge="b-type"
    def __init__(self,br,pr):
        self.brand=br
        self.price=pr
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("charge type:",self.charge)

phone.charge="c-type"

sam=phone("samsung","2000")
red=phone("redmi","1000")
sam.display()
red.display()
