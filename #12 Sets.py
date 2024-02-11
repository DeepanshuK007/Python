'''
Sets are unordered collection of data items. 
They store multiple items in a single var
Seperated by commas and enclosed in curly brackets.
!!!Immutable, no duplicate items.!!! 
'''

info = {'Deep', 6.2, 3, '!'}
print (info)

for i in info:
    print (i, end=' ') # u will notice that the order of the elements appearing is not the same as og
#Thus there is no gaurantee of order
print ('\n')
    
#Joining Sets & Set Methods:
# 1.union() and update():
# union creates a new set whereas update updates the value in the same set
cities = {'Mohali', 'Chandigarh', 'Kharar', 'Thane'}
cities1 = {'Thane', 'Bandra', 'Mira Road'}
# print (cities.union(cities1))  # new set
# print (cities.update(cities1)) # upadtes cities

# # 2.intersection() and intersection_update()
# # Prints only items that are similar to both the sets.
# print (cities.intersection(cities1))  # creates a new set
# print (cities.intersection_update(cities1)) #updates the same set

# 4.symmetric_difference and symmetric_difference_update()
# These methods only prints the items that are not similar to both the sets. 
print (cities.symmetric_difference(cities1))  # creates a new set removes Thane
print (cities.symmetric_difference_update(cities1)) #updates the same set



