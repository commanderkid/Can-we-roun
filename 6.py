ln=int(input())
c=[]
for i in range(ln):
    m=input().split()
    if "-" in m:
        a=m[1:]
    else:
        a=m
    a=[int(a) for a in m]
    a=a[0]/a[1]
    a=list(str(a))
    if "." in a:
        b=a.index(".")
        if int(a[b+1])>=5:
            a=a[:b]
            a=''.join(a)
            if "-" in m:
                a="-"+str(int(a)+1)
            else:
                a=str(int(a)+1)
        else:
            a=a[:b]
            a=''.join(a)
            if "-" in m:
                a="-"+str(a)
            else:
                a=str(a)
    else:
        if "-" in m:
            a="-"+"".join(a)
        else:    
            a=''.join(a)  
    c.append(a)
print(' '.join(c))
  


