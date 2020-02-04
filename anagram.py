a=list(input())
b=list(input())
l1=len(a)
l2=len(b)
c=0
if l1==l2:
    for i in a:
        if i in b:
            c=c+1
    print('yoyo') if c==l1 else print('xoxo')     
else:
    print('xoxo')             