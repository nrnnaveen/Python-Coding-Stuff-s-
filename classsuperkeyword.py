class a():
    def __init__(self):
        print("A")
class b(a):
    def __init__(self):
        super().__init__()
        print("B")
class c(b):
    def __init__(self):
        super().__init__()
        print("C")


ram=c()
