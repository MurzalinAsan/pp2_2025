mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}
print(mydict)

mydict = dict(name = "John", country = "Canada", age = "36")
print(mydict)

mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}
print(mydict["colour"]) #this should output black because we're refering to the key 'color'

mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}
x = mydict.get("brand")
print(x)


mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}

print(mydict.keys())
mydict["size"] = "big"
print(mydict.keys())
x = mydict.items()
print(x)


mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}

if "brand" in mydict:
    print("yes, brand is in mydict")



mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}
mydict["size"] = "XL" #adds a new key and its value to the dictionary((also can be done using the update() function))   
mydict.update({"year": "2020"}) #changes the value of the key
print(mydict)


mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}
mydict.pop("colour")
print(mydict)


for x, y in mydict.items():
  print(x, y)


mydict = {
    "brand": "hilfiger",
    "name": "jacket",
    "year": "2010",
    "colour": "black"   
}

dict2 = mydict.copy()
print(dict2) #dict2 is a copy of mydict


#nested dictionaries

mydict = {
   "dict1": {
      "brand": "hilfiger",
      "name": "jacket",
      "year": "2010",
      "colour": "black" 
   },  
   "dict2": {
      "brand": "armani",
      "name": "jacket",
      "year": "2005",
      "colour": "brown" 
   },
   "dict3": {
      "brand": "adidas",
      "name": "jacket",
      "year": "2020",
      "colour": "white" 
   }

   
}

#to access:
print(mydict["dict1"]["brand"])

#or:

for x, y in mydict.items():
   print(x)
   for z in y:
      print(z + ':' + y[z])

    




