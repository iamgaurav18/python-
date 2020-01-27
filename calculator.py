o=input('Enter a operator:')
a=float(input('Enter operand 1:'))
b=float(input('Enter operand 2:'))
if o=='+':
    c=a+b
elif o=='-':
    c=a-b
elif o=='*':
    c=a*b
else:
    c=a/b
print(c)    
