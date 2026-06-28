#creat a class laptop and add varibles(price,process,ram)
#creat objects(hp,lenovo,dell)
class laptop:
    price:""
    processor:""
    ram:""
hp=laptop()
lenovo=laptop()
dell=laptop()
hp.price=50000
hp.processor="i5"
hp.ram="8gb"
lenovo.price=66000
lenovo.processor="i6"
lenovo.ram="4gb"
dell.price=77000
dell.processor="i7"
dell.ram="12gb"
print("Hp price:",hp.price)
print("hp processor:",hp.processor)
print("hp ram:",hp.ram)
print("............")
print("Lenovo price:",lenovo.price)
print("lenovo processor:",lenovo.processor)
print("lenovo ram:",lenovo.ram)
print("..............")
print("Dell price:",dell.price)
print("dell processor:",dell.processor)
print("dell ram:",dell.ram)
print("................")
