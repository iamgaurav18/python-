def abc(n):
    if(n==0):
        return
    abc(n//2)
    print(n%2,end='')

abc(13)        