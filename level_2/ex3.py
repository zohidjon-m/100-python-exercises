'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
in_put = input("enter: ")
lis = [x for x in in_put.split(',')]
lis.sort()
#for i in range(len(lis)):
    #print(lis[i])

print(','.join(lis))