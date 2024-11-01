'''
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number 
between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''

def integer(x):
    diic = {}
    for i in range(1, x+1):
       k = i*i
       diic[i] = k
    
    return diic

x = int(input("enter an integer: "))
if x == 0:
    print("It should be above than 0")
else:
   reselut = integer(x)     

print(reselut)