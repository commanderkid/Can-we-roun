qp=int(input())
c=[]
for i in range(qp):
    a=input()
    a=a.split()
    a=[int(a) for a in a]
    a=a[0]/a[1]
    if int(a)==float(a):
        c.append(int(a))
    else:
        a=list(str(a))
        m=a.index(".")
        n=int(a[m+1])
        a=''.join(a[0:m])
        if '-' in a:
            a=int(a)
            if n<=5:
                c.append(a)
            else:
                c.append(a-1)
        else:
            a=int(a)
            if n>=5:
                c.append(a+1)
            else:
                c.append(a)
print(' '.join([str(c) for c in c]))
                
    
