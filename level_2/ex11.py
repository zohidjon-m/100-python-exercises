'''
Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
'''
from math import sqrt

def odd(num):
    k = []
    for i in num:
        if i % 2 != 0:
            k.append(i)   
    return k

num = input("enter: ")
num = [int(x) for x in num.split(",")]
result = odd(num)
l = []
for i in result:
    m = sqrt(i)
    l.append(m)
    
print(result)
print(l)
'''
input_numbers = input("enter: ")

numbers = [int(x) for x in input_numbers.split(",") if int(x) % 2 != 0]
result = [str(num**2) for num in numbers]
print(",".join(result))