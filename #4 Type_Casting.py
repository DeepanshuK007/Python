a = "1"
b = "2"
print (a + b) 
# Here the output comes out to be as 12 as the nums entered are in the form of a string
print (int(a) + int(b))
# HEre we have typeCasted the above string an dthus it comes out to be 3.
# The above exampes are of Explicit Conversions

#Implicit Convresions:
# Some of the datatypeshave higher order than that of the others such as float has higher priority over int. In such case the variable with lower datatype will be implicitly get converted to higher while operating.

# Python does this to prevent data loss.
c = 1.9
d = 4
print ("Implicit Conversion: ", (c + d), "and type is: ", type(c+d))


#-----------------------User Input-------------------------------------
# We can take input using input() func and this returns a string or char thus we have to store it in a var.

# i = input("Enter your name: ")
# print (i)
i = input ()
print (i)