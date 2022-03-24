'''
18.Write a python program that takes a integer number from the user and displays 
the reversed number.

S#	Input	Output
(i)	Enter a number: 523	Reversed number: 325
(ii)	Enter a number: 12	Reversed number: 21
'''

n = int(input("Enter a number: "))
re = 0
while (n>0):
    r = n% 10
    re = re * 10 + r
    n = n//10

print(re)