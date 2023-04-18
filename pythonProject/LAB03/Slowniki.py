"""
Słowniki
"""

#tworzenie

thisdict = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002
}
print(thisdict)

print()

#wyswitlenie z klucza

thisdict = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002
}
print(thisdict["brand"])

print()

#Print the number of items in the dictionary

thisdict = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002,
  "speed": 250
}
print(len(thisdict))

print()

#The values in dictionary items can be of any data type

thisdict = {
  "brand": "Mazda",
  "electric": False,
  "year": 2002,
  "speed": 250,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

print()

#Type
#From Python's perspective, dictionaries are defined as objects with the data type 'dict'

""""
<class 'dict'>
"""

thisdict = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002
}
print(type(thisdict))

print()

#The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary

thisdict = dict(brand = "Mazda", model = "RX-7", year = 2002)
print(thisdict)

print()

"""
Accessing Items
"""

#You can access the items of a dictionary by referring to its key name, inside square brackets

thisdict = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002
}
x = thisdict["model"]
print(x)

print()

#There is also a method called get() that will give you the same result

thisdict = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002
}
x = thisdict.get("model")
print(x)

print()

"""
Get Keys
"""

#The keys() method will return a list of all the keys in the dictionary

thisdict = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002
}
x = thisdict.keys()
print(x)

print()

#Add a new item to the original dictionary, and see that the keys list gets updated as well

car = {
  "brand": "Mazda",
  "model": "RX-7",
  "year": 2002
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
