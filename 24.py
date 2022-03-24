'''
24.Write a python program that takes a number from the user and checks 
if it is an Armstrong number. An Armstrong number is an integer such 
that the sum of the cubes of its digits is equal to the number itself. 
153 is an Armstrong number because  13+53+33  is equal to 153

S#	Input	Output
(i)	Enter a integer: 6	Perfect
(ii)	Enter a integer: 10	Not perfect
(iii)	Enter a integer: 496	Perfect
'''


num = int(input("Enter a integer:"))
d  = int(len(str(num)))
sum = 0
x = num
while(num > 0):  
    c = num % 10
    sum = sum + c**d
    num = num // 10 # 15 


if (sum == x):
    print("Perfect")
else:
    print("not Perfect")