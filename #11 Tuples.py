''' 
Tuples are ordered collection of data items.
They store multiple items in a single var.
Once created they cannot be modified.
'''

# Tuple Indexes:
# 1 Each item in a tuple has its own unique index.
# 2 This index can be used to access any particular item from the tuple

#Accessing tuple items:
#1. Positive Indexing:
country = ("Spain", "Italy", "India", "England", "Germany")
print (country[0])
print (country[1])
print (country[2]) #Each item is stored at an index.

#2. Negative Indexing:
print (country[-1]) #country.len() - 1

#3. Check for item:
# We can check if a given item is present in the tuple. This is done using the in keyword
if 'England' in country:
    print ("Present")
else:
    print ("Absent") 

# 4. Range of Index:
#U can print range of tuple items by specifying where do you want to start, where do u want to end and if ypu want to skip elements in between the range
    #0 based indexing
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print (animals[3: 7]) #from 0 -> 6
print (animals[-6: -2])

print (animals[4: ]) #from 4 to the end
print (animals[-4: ]) # When subtracting subtract from the length.

print (animals[ :7])

print (animals[ : :3])

# Manipulating Tuples & Tuple Methods

# As tuples are immutable hence if u want to add, remove or update the tuple values then u first must convert the tuple to a list, do the operations and then convert it back to tuple. 
temp = list(animals)
temp.append("quail")
temp.pop(3) #mouse
temp[2] = "lion"
animals = tuple(temp)
print (animals)

# Concatinating two tuples:
countries = ('Austri', 'India', "USA", 'Melborne')
countries1 = ('Swedan', 'Norway', 'PAK')
Tcountry = countries + countries1
print (Tcountry)

#Tuple Methods:
# 1.count()- Returns the no of times the gievn element apperts in the tuple.
print (Tcountry.count('India'))

# 2.index()- Returns the first occurrence of the given element
print (Tcountry.index('Melborne')) # 0 based indexing

























































































