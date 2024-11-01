'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible 
by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

in_put = input("Enter: ")
lis = in_put.split(',')

alis = [int(num) for num in lis if int(num) % 5 == 0]
for i in range(alis):
    print(i)
        