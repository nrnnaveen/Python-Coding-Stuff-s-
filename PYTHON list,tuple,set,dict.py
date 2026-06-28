#PYTHON COLLECTIONS (ARRAYS)

# THESE ARE FOUR COLLECTION DATA TYPES IN THE PYTHON PROGRAMING LANGUAGE


#"LIST" : is a collection which is ordered and changeble ,allows duplicate members

#"TUPLE" :is a collection which is ordered and UNchangeble ,allows duplicate members 

#"SET" :is a collection which is unordered and unchangeble ,and un index no duplicate members

#"DICTIONARY" : is a collection which is ordered and changeble ,no duplicate members

#1

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
#its means 0=1,1=2,2=3,3=4,4=5,5=6


#2

#tuple()
#allows duplicate
#any type of data can be stored
#we can not moddify the tupple item . we cannot add or remove
a=(1,3)


#3

#set{}
#do not allow dupilicate
#any type of data can be stored
#we can not modify the set items
#we can add or remove set items
#sets are unordered
#(add(),update(),remove(),pop())
a={1,2,3,4,5,6}
print(a)
a.remove(5)#remove the number 5 in the list a
print(a)
a.add(7)#add the number 7 in the list a
print(a)
a.pop()#sets are unordered so its remove the first letter in the list a
print(a)
a.update()#not clear explain
print(a)


#4

#dictionary{}
#do not allow dupilicate values will overwrite existing values
#any type of data can be stored
#key:value pair,eg:("name":"EMC")
#{get(),keys(),values(),items(),update(eg:{"year":2025}),thisdict["colour"]="red",
#thisdict(pop("model")),del,clear}
#

a={
    "name":"emc",#use comma, for every line to use dict
    "age":1,
    "place":"vkl",
    "sub":"eng"
    }

print(a)
print(a.keys())#get the keys in the dictionary
print(a.values())#to get the values in the dictionary
print(a.items())#to get all items in the dict
a["age"]=2#update items in dict
print(a)
a.update({"place":"vellankovil"})#update items in dict
print(a)
a["colour"]="red"#add items in dict
print(a)
a["year"]=2025#add items in dict
print(a)
del a["sub"]#del particular items in dict and you can also use the pop
print(a)
a.clear()#clear all items in dict
print(a)

#you can use 2 methed of update(a[]= , a.update({}))
#you can use 2 methad of delete(pop ,del a[])

