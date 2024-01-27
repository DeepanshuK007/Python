# Execution in python takes place line by line.
print ('Hello'),
print (2),
print ('Love', 2) #Here we can take many inputs to print something of diff datatypes.
print (12*4)

# Escape Sequence Characters-
print ("Hey there, \n Deepanshu \t here!")                                     
#n is used to move to the next line and \t is used to have a tab space.

print ("I am a \'proficient \"learner\"\'!")
#To put somting in single\double invered commas use \'\"abc\'

#OPTIONAL
# If u want to put some seperator after every datatype then use:
print ("Use of seperators:", 1, 2.4, sep=' ~ ', end=' !\n')
#U can also end the line by the syntax end=''

# Data Types:
#Sequenced Data: Lists, Tuple, range

a = 1,
b = True,
c = 'Harry',  # The content in single inverted is Tulpe
d = "Deep"    # The content in double inverted commas is String
e = None
a1 = 1 + 1.1, # Here teh operations for diff datatypes is simply possible
a2 = 2 + complex(6, 2)
# print (a + a1)
print ("The type of a is: ", type(a))
print ("The type of b is: ", type(b))
print ("The type of c is: ", type(c))
print ("The type of d is: ", type(d))
print (a2)
print ("The type of a2 is: ", type(a2))
print ("The type of e is: ", type(e))

'''Lists: 
A list is an ordered collection of data with elements seperated by a comma and enclosed within square brackets.
Lists are mutable and can be modified after creation.'''
list1 = [8, 6, 5, [-5, [0]], ['Apple, 1'], 'Mango']
print (list1) 

# Lists are mutable but tuples are non mutable.
tuple1 = (('parrot', 'bird'), ('Cheetah', 'animal'))
print (tuple1)

#Mapped Data: Dictionary
# An unordered collection of data consisting of key:value pair. The key:value pair are enclosed within curly brackets.
dict1 = {"name":"Viraj", "age":"20", "isMan":True}
print (dict1)

# Imp!!!!- When u print the type of each var above the datatype comes as a class: ''. This is because 'everything in python is a Object'