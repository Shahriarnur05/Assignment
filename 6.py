'''
6. Write a python program that takes two integers from the user and 
dispalys all the odd numbers between them. Make sure there is no extra comma.

S#	Input	Output
(i)	Enter two integer numbers: 5 10	5, 7, 9
(ii)	Enter two integer numbers: 8 8	'''

x , y = [int (x) for x in input("Enter two integer numbers: ").split()]

for i in range(x, y+1):
    if (i%2 != 0):
        if(i<y+1):
            print(i,end=",")
        