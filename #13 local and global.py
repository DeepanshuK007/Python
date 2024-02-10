'''
local variable- The one which is defined inside a func and accessible within that function.
It is created when the func is called and is destroyed when the function returns.
A global var is a var that is defined outside of a func and is accessible from within any func in your code. 
'''

x = 10
def func() :
    y = 5
    print (y)
    print (x)  # global var accessible within a func

func()
print(x)
# print(y) # shows an error as y is not global var

# The global keyword:
x = 10
def func():
    global x # we have used the global keyword to declare that we want to modify ht eglobal var x from within the func
    x = 5
    y = 5

func()
print (x)
#print (y)

# We should avoid modifying global vars from within the functions, as it can lead to unexpected behavior and make code harder ro debug.

