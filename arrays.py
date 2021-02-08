import sys

# Array exercises

# create an array of 5 integers and ddisplay the first 3 items
array1 = [7, 9, 2, 8, 1]

for n in range(0, 3):
    print(array1[n])

# append a new item
array1.append (11)
print(array1)

# reverse the order of the items
newList = []
for a in reversed(range(0, len(array1))):
    newList.append(array1[a])
print(newList)

# lenght in bytes of element
print("Memory size of", str(array1[0]), "is", str(sys.getsizeof(array1[0])), "bytes.")
