fruits = ["apple", "orange", "banana", "cherry"]        #list 
print(fruits)
print(fruits[0])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])             #reversed version

for fruit in fruits :
    print(fruit)


print(dir(fruits))              # prints all functions related to collection
print(help(fruits))                       #explaining all functions 
print(len(fruits))              # length of collection 
print('apple' in fruits)         #bool

fruits[0] = 'pineapple'          #change index 
fruits.append("apple")              #adds new fruit
fruits.remove("apple")
fruits.insert(0, "tomato")        #inserting new value to given index 
fruits.sort()                     #sorting for alphabetic order 
fruits.reverse()                  #reversing the collection
fruits.index("tomato")            #finding the index of given value 
fruits.count("banana")            #finding the number of bananas 
fruits.clear()                    #deleting everything


cars = {"bmw", "merc", "audi"}
print(cars)
print(len(cars))
cars.add("rolls")              #adds new car
cars.remove("merc")            #deletes the given value 
cars.pop()                      #removes the first element
cars.clear()

subjects = ("cs", "math", "english")
print(subjects.index("math"))
print(subjects.count("cs"))
