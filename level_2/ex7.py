'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is
an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

k = []
for j in range(1000, 3001):
    s = str(j)
    all_even = True
    
    for digit in s:
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        k.append(s)
            

print(",".join(k))