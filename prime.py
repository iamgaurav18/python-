n=int(input("enter a number:"))
c=0
i=n
while i>0:
    a=n%i
    if a==0:
        c=c+1
    i=i-1    
print('prime') if c==2 else print('not prime')    

