#list[]
#allows dupilicat
#any type of data can be stored
#we can modify the list item ,we can add or remove
#(insert(),append(),extend(),pop())

a=[1,2,3,4,5,6,]
b=[11,12,13,14]
print(type(a))#what the type of a is
a.append(7)#add the number 7 in the list of a lastly
print(a)
a.insert(0,8)#insert the number 8 in the 0th position first
print(a)
a[1]=8#insert the number 8 in the list and remove 1 in the list
print(a)
a.pop(0)#remove the first value in the list
print(a)
#a.pop()atomaticaly remove last number in the list
a.extend(b)#add the (b) list in the (a) list lastly
print(a)

#index values will be consider
#   a=[1,2,3,4,5,6,]
#index[0,1,2,3,4,5,]
#its mean 0=1,1=2,2=3,3=4,4=5,5=6
