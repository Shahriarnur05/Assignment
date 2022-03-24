'''
2. Write a python program that displays the following number sequence. 
Make sure there is no extra comma.

Number Sequence: 0,1,2,3,...,99'''

n = 0
for i in range (1 , 100):
    if (1< i <= 99):
        print(end= ",")
    print(i,end="")
