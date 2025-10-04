capitals = {"USA" : "Washington DC", 
            "Azerbaijan" : "Baku", 
            "Turkiye" : "Ankara"}

print(capitals.get("Turkiye"))             #getting value of key

capitals.update({"Germany" : "Berlin"})       #adds new key and value to the collection or changes the value of key
capitals.pop("USA")                        #removes the key and the value of key, but you cannot remove the last item with this funtion
capitals.popitem()                         #removes the last key and value
keys = capitals.keys()                      #getting only keys not values
for key in capitals.keys() :
    print(key)
values = capitals.values()                 #getting only values not keys
for value in capitals.values() :           
    print(value)

for key, value in capitals.items() :
    print(f"{key} : {value}")

