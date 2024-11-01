'''
Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import re
input_password = input("Password: ")
password = [x for x in input_password.split(",")]
l = []
for i in password:
     
    #first way: non-regular expression
    '''
    if any(k.isalnum() for k in i) and any(k.isalpha() for k in i) and any(k.isdigit() for k in i) and any(k.islower() for k in i) and any(k.isupper() for k in i) and 6<=len(i)<=12:
         
       print("all good")
        
       l.append(i)
        
    else:
       print("invalid password")
         
#print(",".join(l))
'''

     
    if len(i)<6 or len(i)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",i):
        continue
    elif not re.search("[0-9]",i):
        continue
    elif not re.search("[A-Z]",i):
        continue
    elif not re.search("[$#@]",i):
        continue
    elif re.search("\s",i):
        continue
    else:
        pass
    l.append(i)
print(",".join(l))