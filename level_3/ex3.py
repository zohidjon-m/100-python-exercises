''''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

'''
from typing import Any


class divisibleBySeven:
    def __init__ (self, n):
        self.n = n
        
    def get_num(self):
       for i in range(0, self.n +1):
           if self.n%7 == 0:
                yield i
            
a = int(input("enter: "))
gen_seven = divisibleBySeven(a)
for num in gen_seven.get_num():
    print(num)