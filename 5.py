'''
5. Write a python program that takes two integers from the user and dispalys 
all the integers between them including the input numbers. Make sure there 
is no extra comma.

S#	Input	Output
(i)	Enter two integer numbers: 5 10	5, 6, 7, 8, 9, 10
(ii)	Enter two integer numbers: 0 0	0'''

x, y = [int (x) for x in input("Enter two integer numbers: ").split()]

for i in range (x , y+1):
    if (i != x):
        print(end=",")
    print(i,end="")

