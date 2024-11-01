'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

'''

class String:
    def getString(self):
        x = input(" enter str: ")
        return x
    
    def printString(self, myString):
        print(myString.upper())
        
        

# Test function
manipulator = String()
user_string = manipulator.getString()

manipulator.printString(user_string)
