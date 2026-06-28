"""
creat a class call vehicle and add property start to print vehicle start
creat derived class called car and add property start to overite
the vehicle started into car started
"""
class vehicle():
    def start(self):
        print("VEHICLE STARTED")
class car(vehicle):
    def start(self):
        print("CAR STARTED")

a=car()
a.start()

