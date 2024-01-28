# MultiLine Strings are executed using triple double inverted commas ("""/''')
a = """hfsjehfgahgh
    MKEWNKJNJNKJEW
    EKnjvEBJE"""
print (a)
print ('\n')

# Accessing Characters of a string:
name = "Deepanshu"
print (name[4]) # Here too indexing starts from 0 to .., [4] returns 'a'

# Looping through a string
for character in name:  # Here character is like in ti in C(iteration var)
    print (character)

# String Slicing and Operations
names = "Viraj, Rahul"
print (names[0: 5]) # String Slicing, this reads from 0 to 4th index
print (names[ : 5]) # Same output as above as if the starting index is not given then taken as 0. 
print (len(names)) 
print (names[0 : -3]) # If u mention something in -x then it does the opeartion 'len(names) - x'
print (names[-7: -3])   



