"""
1. Lists are ordered collection of data items.
2. They store multiple items in a single var
3. List items are seperated by commas and enclosed within sqare bracts[]
4. Lists are changeable meaning which we can alter them after creation.
"""

l1 = [1, 2, 3, 4, 5]
l2 = ["Red", "Green", "Blue"]
print (l1, l2)

details = ["Abhijeet", 18, "BvYH$", 20.1]
print (details)

# As we can see that a single list can contain items of diff data types.

# -----------------List Methods-----------------------
# 1. list.sort(): Sorts in ascending order.
colors = ['magenta', 'turquiose', 'beige', 'maroon']
colors.sort()
print(colors)

num = [10, 9 , 8, 7, 6, 5]
num.sort()
print (num)

colors.sort(reverse=True)  # print in decending order
print(colors)

# 2 reverse()- This reverses the order
num.reverse()
print (num)

# 3 index()- This method returns the first index of the first occurrence of the list item.
colors1 = ['violet', 'green', 'blue', 'black', 'pink']
print (colors1.index('pink'))  # 0
print (num.index(5)) # 5

# 4 count()- Returns the count of the number of items with the given value.
num1 = [1, 5, 4, 7, 9, 7]
print (num1.count(7))

# 5 copy()- Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
colors_copy = colors1.copy()
print (colors1)
print (colors_copy)

# 6 append()- This appends items to the end of the existing list
colors1.append('grey')
print (colors1)

# 7 insert(): This method inserts an item at the given index.
colors1.insert(2, 'brown') #0 based indexing
print (colors1)

# 8 extend(): This method adds an entire list or other datatype (set, tuple, dictionary) to the existing list.
colors1.extend(colors)
print (colors1)

tuple= (1, (5, 4))
dict = {"car": 'ford', 'bike':'dicarti'}
list = [1, [2, [3, [4]]]]
print (num.extend(list))  # None - as both the datatyes should be same and also appends single arg at a time. Such a shame!

# 9 Concating two lists:
print (colors + colors1) # same work as extend
