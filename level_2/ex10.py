'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
'''result = 0
a = int(input("enter only an integer: "))

aa = str(a) + str(a)
aaa = str(a) + aa
aaaa = str(a) + aaa
result = int(a) + int(aa) + int(aaa) + int(aaaa)
print(result)
'''

a = int(input("Enter an integer: "))

result = 0
for i in range(1,5):
    result += int(str(a) * i)
    
print(result)