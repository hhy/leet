'''
n bricks,
require stack a stair:
unique number of brick for each step
q: how many combination for given n

n=3 => 1
*
**

n=4 => 1
*
*
**

n=5 => 2

*
**
**

*
*
*
**
'''




def fs(n, k=1, s=0, l=[]):
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

def fk(ns, mini, k):
    ss=ns
    if ss <= k*mini:
        return 0
    
    if k==2:
        if ss%2==0:
            return ss/2-mini
        return (ss +1)/2-mini
    
    max = ss/k
    if max<=mini:
        return 0
    
    cnt=0
    for i in range(mini, max):
        cnt+=fk(ns-i, i+1, k-1)
    return cnt

def fkk(ns, mini, k):
    ns, k= ns-mini*k, k
    
    return fk(ns, 0, k)





def f(n, ff):
    t=int( ( (8*n+1)**0.5-1 )/2 )
    c=0
    for i in range(2, t+1):
       c+=ff(n-i, 0, i)
    return c

def g(n):
    myd=dict()
    def gk(ns, k):
        if ns*1000+k in myd:
            return myd[ns*1000+k]
        
        if ns <= 0:
            return 0
        if k==2:
            if ns%2==0:
                rr=ns/2
            rr= (ns +1)/2
            return rr
 
        max = ns/k
        if max<=0:
            return 0
    
        cnt=0
        for i in range(0, max):
            myns, myk=(ns-i)-(i+1)*(k-1), k-1
            cc=gk(myns, myk)
            cnt+=cc
            myd[myns*1000+myk]= cc
            
        myd[ns*1000+k]=cnt
        return cnt

    t=int( ( (8*n+1)**0.5-1 )/2 )
    c=0
    for i in range(2, t+1):
       c+=gk(n-i, i)
    #print myd
    return c



#print f(10)

n=150
import time
for n in [180, 190,200, 1000]:
    aa= time.time()
    #u= gs(n)-1
    u= g(n)
    bb= time.time()
    print n, u, bb-aa
    #u= f(n, fk)
    aa= time.time()
    #print n, u, aa-bb





        
