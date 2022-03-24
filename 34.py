def palindrome(n):
    st = 0
    end = len(n) - 1
    while ( st < end):
        if (n[st] != n[end]):
            return "False"
            break
        else: 
            return "True"
            break
        st += 1
        end -= 1
        
n = input("Enter a integer: ")
print(palindrome(n))