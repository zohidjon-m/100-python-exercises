'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
upper = 0
lower = 0
sentence = input("Enter: ")

for x in sentence:
    if x.isupper():
        upper+=1
    elif x.islower():
        lower+=1
    else:
        pass

print(f"UPPER CASE {upper}\nLOWER CASE {lower}")