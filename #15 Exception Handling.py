# Exception handling deals with the problems to avoid system crashing, and without this process, exceptions would disrupt the normal execution of the program.

#Python has many build in exception sthat are raised when your program encounters an error

#When an exception occurs python interpretor stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash

# Python try...except
# try...except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error, if an error is caught by the try block it is addressed by the except block

try:
    # Statement that could generate exceptions
    num = int(input("Enter an integer: "))
except:
    # Sol for the exception occured
    print ("Num entered is not an int")

# The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing db connection or may be ending the prog execution with a delighful message.
    
# The finally block will execute in any situation irrespective of try...except...else blocks
    
try:
    num = int(input("Enter an integer: "))
except:
    print("Enetr a valid int")
else:
    print("Integer Accepted")
finally:
    print("This block is always executed.")

#Raising Custom errors:
salary = int(input("Enter Salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError()