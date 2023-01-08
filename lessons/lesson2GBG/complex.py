print("________________List/string________________")

list1 = [[[[[1]]]]]
list2 = list()

list3 = [1,2,3,4,5,6,7,8,9,10]
list4 = list(["hej","På","Dig",True])

list5 = [list3,list4]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

print(list1[0][0][0][0][0])
print(list4[0])

greeting = list4[0]
print(greeting)
print(list4)

list_length = len(list3)
print(list_length)
print(list3[len(list3)-1])
print(list3[-1])
print(list3[-2])

#list6 = list3 Får samma address i minet ,dvs är samma array och alla operationer kommer att påverka båda
list6 = list3.copy()
print(list3)
print(list6)

list6[0] = 1337
list6.append("Tjollahopps")
list6.insert(6,"Tjabba tjena")
print(list3)
print(list6)

print(hex(id(list3)))
print(hex(id(list6)))
print(hex(id(list4)))

new_list = list6[:]
print(new_list)

new_list = list6[2:5]
print(new_list)

new_list = list6[2:]
print(new_list)

new_list = list6[:5]
print(new_list)

second_list = list6[-4:]
print(second_list)


sliced_list = new_list + second_list
print(new_list,second_list,sliced_list)

my_string = "Hello my name is what?"
print(my_string[:5])
print(len(my_string))

print(list(my_string))

#my_string[0] = "Y"  #Funkar inte eftersom strängar är immutable


print("")
print("_______________Set _____________________")

set_list = [1,1,1,5,5,"Anton","Anton","Anton","Anton","Anton","Hej",True,True,True,True,True,False]

set1 = set()
set2 = {"Anton","Sven","Anton","Anton","Anton","Anton"}

set3  = set(set_list)


value = set3.pop()

print(value)
print(set3)
print(set2)

print("")
print("______________Tuples______________")

tuple1 = ()
tuple2 = ("Anton",30,"Developer","Anton")

tuple3 = tuple((456,"Tolv"))

print(tuple1)
print(tuple2)

name,age,role,another_name=tuple2
print(name,age,role,another_name)

name ="hej"
print(name,age,role)
print(tuple2)


print("")
print("_______________dictionaries_____________")

#Dictionaries bygger key,value pairs.

dict1 = {}
dict2 = dict()

dict3 = dict({})
dict4 = {
  1:"One",
  "greeting":"Hello",
  (2,3,4):"Tjogräs",
  False:[1,2,3],
  name:"Tjka"
}

anton = {
  "name":"Anton",
  "age":30,
  "company":{
    "name":"Mujina",
    "location":"STHLM"
  },
  "pets":[
    {"name":"Shirokumakun",
     "color":"white",
     "age":25
    }
  ]
}

print(dict4)
print(anton)

name = anton["name"]
name = anton.get("name")
#name = anton.get("asdr") #Ger none om det inte finns
print(name)

company_name = anton["company"]["name"]
print(company_name)

first_pet = anton["pets"][0]["name"]
print(first_pet)

fjanton = anton
print(fjanton)
fjanton["name"]  ="Fjanton"
print(anton)

print(hex(id(fjanton)),hex(id(anton)))

keys = anton.keys()
values = anton.values()
key_value = anton.items()
print(keys)
print(values)
print(key_value)