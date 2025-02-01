mylist = ["toyota", "sony", "samsung"]

thislist = ["toyota", "sony", "samsung"]
print(len(thislist)) #returns the length of the list

list1 = ["bracelet", False, 34]#can contain different data types


thislist4 = list(("toyota", "sony", "samsung"))
print(thislist4)



thelist = ["toyota", "sony", "samsung"]
print(thelist[1]) #returns the element of the list with index 1

dalist = ["toyota", "sony", "samsung"]
if "toyota" in dalist:
    print("Yes, toyota is in the list") #checks whether an pbject is present in the list



thislist = [["toyota", "sony", "samsung"]]
thislist.insert(2, "jacket")
print(thislist)

myList1 = ["toyota", "sony", "samsung"]
myList2 = ["calculator", "fridge"]
myList1.extend(myList2)
print(myList1)


mylist = ["toyota", "sony", "samsung"]
mylist.pop(1)
print(mylist)

mylist = ["toyota", "sony", "samsung"]
del mylist[0]
print(mylist)

thislist = ["toyota", "sony", "samsung"]
for x in thislist:
    print(x)

thislist = ["toyota", "sony", "samsung"]
[print(x) for x in thislist]

companies = ["toyota", "sony", "samsung"]
newlist = [x for x in companies if "a" in x]
print(newlist)

list1 = ["toyota", "sony", "samsung"]
list1.sort()
print(list1)

list1 = ["toyota", "sony", "samsung"]
list2 = list1.copy()
print(list2)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

