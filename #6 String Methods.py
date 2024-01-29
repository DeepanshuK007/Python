# String Methods:
#1. upper(): The upper() method converts a string to upper case.
tag = 'maveric!'
print (tag.upper())  # MAVERIC

#2. lower()
tag1 = "MaveRic"
print (tag1.lower()) # maveric

#3 strip(): This method removes all the white spaces before and after the string, but not in between.
tag2 = '  Mave ric!!    '
print(tag2.strip())

#4 rstrip(): Removes any trailing characters, specified as arguments.
print(tag.rstrip("ric!"))

#5 replace(): This method replaces replaces all the occurences of a specified string wiht thh ereq ones.
print (tag.replace('maveric', 'rooster'))

#6 split(): This method splits the string at the specified instance and returns the seperated as list.
print (tag2.split(' '))

#7 capitalize(): This method only turns thhe first character of the string to uppercase and the rest other characters are lower cases.
print (tag.capitalize()) # Maveric


#8 centre(): This methos centers the string witht the marginLeft mentioned as param.
print (tag.center(70, '-'))
# The sec param entered gets filled up in the remaning space horizontally.

#9 count(): Returns the number of times a given string has occured
print (tag2.count(' '))  # 7

#10 endswith(): Checks if the string ends with the given value and ruturns a bool
print (tag1.endswith('Ric'))

print (tag1.endswith('Mave', 0, 4))
# Also u can check for in between elements by specifing the starting index and the index net to the last elem.

#11 find(): Thsi method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
print (tag.find("e")) # 3
print (tag.find("*")) # -1  

#12 index(): This method searches for the first occurrence of the given value and returns the index where it is present.
# If the given value is absent from the string then raise an exception.
print (tag.index('i')) # 5
# print (tag.index('x')) # returns an exception

# This is the diff between the two that index() returns an exception if not present.

#13 isalnum(): Returns true only when when the entire string oly consists of A-Z, a-z, 0-9. If other than these then returns false.
tag3 = 'Maveric007'
print (tag3.isalnum()) # True 

#14 isalpha(): Returns true only when A-Z, a-z are present, any other punctuations or nums are present then returns a false
print(tag3.isalpha()) # False

#14 islower(): Returns true only if all the chars in the string ar inlower else false.
print (tag3.islower()) # False

#15 isprintable(): Returns true only if all the values within the string are printable, if not then False.
print (tag3.isprintable())

#16 isspace(): Returns true only if th estring has white spaces else false.
tag4 = "        "
print (tag4.isspace()) # True

#17 istitle(): Returns true only if the first letter only of the word is capitalized.
print (tag.istitle()) #maveric => False
print (tag1.istitle()) #MaveRic => False as R is caps

#18 isupper(): Returns true only of all the chars are in upper case.
print (tag.isupper()) # false

#19 startswith(): Returns true if the string starts with the given value.
print (tag4.startswith('  '))

#20 swapcase(): This method changes the character casing of the string. Upper case are convereted to lower
print (tag3.swapcase())

#21 title(): This method capitalizes each letter of the word within the string.
print (tag2.title()) # Mave ric! => Mave Ric!

