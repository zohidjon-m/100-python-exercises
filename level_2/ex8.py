'''
Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

'''
letter = 0
number = 0
sentence = input("Enter: ")

for char in sentence:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        number += 1
    else:
        pass
      
print(f"letters: {letter}, digits: {number}")