#poly-method over writing
#creat a clas animal thart have function of sound thats print animal make sound
#creat a derived class dog that inherts from animal that overite sound dogs bark
#creat a another derived class bird that overwrite the sound as bird sing
class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound (self):
        print("dog barks")

class bird (animal):
    def sound (self):
        print("bird sing")

obj=bird()
obj.sound()
