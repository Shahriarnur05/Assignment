'''19.Write a python program that takes two integers from 
the user and 
displays all the numbers between them that are divisible by 7.

S#	Input	Output
(i)	Enter two numbers: 10 50	14 21 28 35 42 49
(ii)	Enter two numbers: 1 5	'''


x , y = [int (x) for x in input("Enter two numbers: ").split()]

for i in range (x,y+1):
    if (i % 7 ==0):
        print(i,end=" ")
