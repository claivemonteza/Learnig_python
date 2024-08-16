

names = ['Claive','Rolando', 'Sousa','Vallejos','Monteza']

# print all list
print(names)

# print all the item on the list from the beging to the end
print(names[:])

# First name on the list
print(names[0])

# Last name on the list
print(names[-1])

# replace a name on the index
names[-1] = 'Vallejos'
print(names)

# Range values
print(names[0:4])

# Will print all the item start with the index 2 to the end the list
print(names[2:])


#LIST METHODS
##Insert method
names.insert(5,'Oliver')
print(names)

##Remove Method
names.remove("Oliver")
print(names)

## remover all items
names.clear()
print(names)


## check is a item existe on list
print('Oliver' in names)

## return a number of item in a list
print(len(names))

## sort
names = ["Carlos", "Ray", "Alex", "Kelly"]
print(sorted(names))
print(names)
print(sorted(names, key=len))

###or
names.sort()
print(names)

## reverse
names.reverse()
print(names)



## 
names.append("Claudia")
print(names)

##
names.pop()
print(names)

## 
names2 = names.copy()
print(names2)

##
print(names.count('Claive'))
