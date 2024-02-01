# Iterating over a string:
name = "Deepanshu"
for i in name:
    print (i, end='.')
print('\n')

# Iterating over a list:
colors = ['Red', 'Blue', 'Yellow', 'Black']
for j in colors:
    print (j, end='|')
# Similarly, we can use loops for lists, sets and dictionaries.
    
#Range in python is used when u want to print a series of numbers.

#Range has arguments such as (start, stop, step). It as optional to include stop and step.
#if u pass onpy one no as arg it is considered as stop no.

series = range(6)  #here 6 is the stop no ans prints the natural nos till 5
for i in series:
    print (i)

s2 = range(2, 6)
for j in s2:
    print (j)
#Output- 2, 3, 4, 5

s3 = range(2, 20, 3)
for k in s3:
    print (k)
#Output- 2, 5, 8, 11,...
    
# While Loop:
# Elecutes or run the loop till the condition is true
count = 5
while (count > 0):
    print (count)
    count= count -1

#Else with while loop: As soon as the wlipe condition becomes false else statement gets executed.
x = 5
while (x > 0):
    print (x)
    x = x-1
else:
    print('Count is at 0')

# Break & Continue Statement:
for l in range(1, 10, 2):
    print (l, end=" ")
    if(l == 7):
        break
    else:
        print ('Lets Go')
print ('Thank U')

#Continue:
for m in [2,3,4,6,8,0]:
    if (m%2!=0):
        continue
    print(m)  # Prints only even nos and skips the rest.