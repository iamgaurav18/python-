def combi(l,lo,hi):
    if lo==hi:
        print(l)
    else:
        for i in range(lo,hi+1):
            l[lo],l[i]=l[i],l[lo]
            combi(l,lo+1,hi)
            l[lo],l[i]=l[i],l[lo]
s=input()
l=list(s)
combi(l,0,len(l)-1)
                