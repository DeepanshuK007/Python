# Built in functions:
#min(), max(), len(), sum(), type(), range(), dict() etc.

# User defined functions:
def func_name(parameters) :
    pass  
    # Code and statements

# Calling a func:
# def name (fname, lname):
#     print ("Hello, " + fname + lname)

# name ("Sam ", 'Altman')

# Func Arguments and Return Statement
# Four types of arguments:
# 1. Default Arguments  2. Keyword Args  3. Variable length args  4. Required Args

# 1. Default Args:
def name (fname, mname= 'Satu ', lname= 'Kashyap'):
    print("Hello, " , fname , mname , lname )

name ('Kartik ')

# 2. Keyword Arguments:
# We can provide arguments with key=value, this way the interpreter recognizes the arguments by the parameter name.

def name (fname, mname, lname):
    print ("Hello, ", fname, mname, lname)

name (mname="Ranvijay", lname= "Singh", fname= "Roop")

# Required Arguments:
def name (fname, mname, lname):
    print ("Hello, ", fname, mname, lname)

name ("Deep", "Deepak", "Danvijay")

#4. Variable-length Arguments:
# Sometimes we may need to pass more arguments than those defined in the actual func. 

# 4a Arbitary Arguments: While creating a func, pass a * before the parameter name while defining the func. The func accesses the arguments by processing them in the form of a tuple.
def name (*name):
    print ("Hello, ", name[0], name[1], name[2])

name ("James", "Janardhan", "Joshi")

# 4b Keyword Arbitrary Arguments:While creating a func, pass ** before the param name while defining the func. The func accesses the arguments by processing them in the form of a dictionary.

def name (**name):
    print ("Hello, ", name["fname"], name["mname"], name['lname'])

name (mname= "Jogardhan", fname= "James", lname= "Champawala")

# return Statement: 
def name (fname, mname, lname):
    return "Hello," + fname + " " + mname + " " + lname

print (name("James", "Buchanan", "Barnes"))
