'''
9.Write a python program that prints Fibonacci series up 
to n terms using loop

S#	Input	Output
(i)	Enter number of terms: 10	Fibonacci series: 0, 1, 1, 2,
3, 5, 8, 13, 21, 34
'''
term = int(input('Enter terms: '))
x = 0
y = 1
count = 0
if (term ==0):
    print(0)
else:
    print("0",end = " ")
while (count<term):
    result = x + y
    x = y
    y = result
    count += 1
    print(y ,end =" ")
