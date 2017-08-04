def fs(n, k=1, s=0, l=[]):
    #mm= (2*n)**0.5 +1
    if k>n:
        return 0
    if s+k>n:
        return 0
    if s+k==n:
        l.append(k)
        print(l)
        return 1
    
    kk=0
    la=list(l)
    kk+=fs(n, k+1, s, la)
    lb=list(l)
    lb.append(k)
    kk+=fs(n, k+1, s+k, lb)
    return kk;

def gs(n, k=1, s=0):
    if k>n:
        return 0
    if s+k>n:
        return 0
    if s+k==n:
        return 1
    
    kk=0
    kk+=gs(n, k+1, s)
    kk+=gs(n, k+1, s+k)
    return kk;
    
        

def f(n):
    def f2(n, s, mini):
        return (n-s)/2 - mini

    def fk(n, k, mini):
        pass

    
    


for n in [3,4,5,6,7]:
    u=gs(n)-1
    #v=f(n)
    print(u)
    
        
