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
a["year"]=2025#add items to dict
print(a)
del a["sub"]#del particular items in dict and you can also use the pop
print(a)
a.clear()#clear all items in dict
print(a)


