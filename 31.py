'''
31. Write a function named reverseNumber that takes an 
integer as parameter and returns the 
reverse number.

For example, the call of reverseNumber(512) should return 215'''
'''
x = input("e : ")
print(reversed(x))'''

x = int(input("Enter a numner: "))

def reverseNumber(x):
    reverse = 0
    while (x > 0):
        reminder = x % 10
        reverse = (reverse* 10) + reminder 
        x  = x // 10
    print(reverse)
reverseNumber(x)
