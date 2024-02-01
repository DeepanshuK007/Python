# Types: if, if-else, if-else-elif, nested if-else-elif
# age = input("Enter your age:")
# if (age> 18) :
#     print("U can drive")
# else:
#     print ("u cannot still!")

# Match case statement similar to switch case statements.
# A match statement will compare a given var value to diff shapes, also reffered to as pattern.
    
x = 4  # x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
        #case with if condition
    case 4 if x % 2 == 0:
        print ("x % 2 == 0 and case is 4")
        # Empty case with if condition
    case _ if x < 10:
        print ("x is < 10")
        # default acse will only be matched if the above cases dont, similar to else
    case _:
        print (x)


