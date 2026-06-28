class goa:
    name=""
    drink=""
    def party (self):
        print("Lets party...")
    def beach (self):
        print("enjoy it...")

ramesh= goa()
suresh= goa()
ramesh.name = "Ramesh"
ramesh.drink = "yes"
suresh.name="Suresh"
suresh.drink="no"
print(ramesh.name)
print("DRINK",ramesh.drink)
ramesh.party()
print("...........")
print(suresh.name)
print("DRINK",suresh.drink)
suresh.beach()
print("............")
