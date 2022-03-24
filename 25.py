'''
25.Write a python program that takes a number from the user and checks if it is 
symmetric(palindrome). A number is symmetric if the reverse of the number is equal 
to the orginal number.

S#	Input	Output
(i)	Enter a integer: 123	Not symmetric
(ii)	Enter a integer: 505	symmetric
(iii)	Enter a integer: 89	Not symmetric
'''

def palindrome(n):
    st = 0
    end = len(n) - 1
    while ( st < end):
        if (n[st] != n[end]):
            print("Not symmetric")
            break
        else: 
            print("symmetric")
            break
        st += 1
        end -= 1
        
n = input("Enter a integer: ")
palindrome(n)
        