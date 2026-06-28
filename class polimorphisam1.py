class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound (self):
        print("dog barks")

class bird (animal):
    def sound (self):
        print("bird sing")

obj1=bird()
obj1.sound()
