'''
3. Write a python program that displays the following number sequence. 
Make sure there is no extra comma.

Number Sequence: 2,2.25,2.50,2.75,...,4'''

n = 2

while (n <= 4):
    print(n,end="")
    if (n < 4 ):
        print(end=",")
    n = n + 0.25
    
    
    

