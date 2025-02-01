thisset = {"pants", "shorts", "shirt"}
print(thisset)

myset  = set(("pants", "shorts", "shirt"))
print(myset)


myset = {"pants", "shorts", "shirt"}
for x in myset:
    print(x)


myset = {"pants", "shorts", "shirt"}
print("pants" in myset)

myset = {"pants", "shorts", "shirt"}
myset.add("car")
print(myset)

myset = {"pants", "shorts", "shirt"}
set2 = {"jacket", "jeans"}
myset.update(set2)
print(myset)


myset = {"pants", "shorts", "shirt"}
myset.discard("pants")
print(myset)

thisset = {"pants", "shorts", "shirt"}

for x in thisset:
    print(x)

set1 = {"pants", "shorts", "shirt"}
set2 = {"jacket", "jeans"}
set3  = set1.union(set2)
print(set3)

