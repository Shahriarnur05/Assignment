'''
4. Write a python program that displays the following number sequence. 
Make sure there is no extra comma.

Number Sequence: 1,3,5,7,...,73'''

n = 1

while (n <= 73):
    print(n,end = "")
    if (n < 73):
        print(end=",")
    n = n + 2