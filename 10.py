'''
10.Write a python program that takes a number from the user 
and calculate its factorial.

S#	Input	Output
(i)	Enter a number: 5	5! = 120
(ii)	Enter a number: 0	0! = 1'''

x  = int(input("Enter a mumber: "))
a = 1
for i in range (1 ,x+1):
    a = i * a

print(a)