'''
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

balance = 0

while True:
   try:
        bInput = int(input("\nEnter 1: Deposit, 2: Withdrawal, 3: Exit.\nEnter: "))
   
        if bInput == 1:
           try:
               deposit = int(input("Enter deposit amount: "))
               balance += deposit
           except ValueError:
               print("Please enter only numbers for the deposit amount!")
        elif bInput == 2:
            try:
                withdrawal = int(input("Enter withdrawal amount: "))
                balance -= withdrawal
            except ValueError:
                print("Please enter only numbers for the withdrawal amount!")
        elif bInput == 3:
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
   except ValueError:
       print("\nInvalid input. Please enter a valid number.")
    
print("Final Balance:", balance)
