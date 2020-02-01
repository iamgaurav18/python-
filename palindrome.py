s=input("Enter a string:")
l=len(s)
t=s[l::-1]
if s==t:
    print("palindrome")
else:
    print("not palindrome")
