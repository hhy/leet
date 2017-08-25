def f(banana_list, r1=0.5):
    
    def willEq(a, b, x,y): # x<y
        if a>b:
            a,b=b, a
        if a==x and y==b:
            return True
        
        if a%2==0:
            c, d=a/2, a/2+b
            if willEq(c,d, x,y):
                return True
        if b%2==0:
            c, d=b/2, b/2+a
            if willEq(c,d, x,y):
                return True
        return False

    def everPlaying(x, y):
        if x==y:
            return False
        if (x+y)%4!=0:
            return True
        if(x>y):
            x,y=y,x
        n=(x+y)/4
        m=not willEq(n, n*3, x,y)
        return m


    def sortM(m):
        lm=len(m)
        l=([(i, sum(m[i])) for i in range(lm)])
        l.sort(lambda a, b: a[1]-b[1])
        k=dict([((x,y), m[y][x]) for x in range(0, lm) for y in range(0, lm)])
        mm=[[k[(l[i][0],l[j][0])] for i in range(0, lm) ]  for j in range(0, lm) ]
        return mm
    
    def pmtx(m):
        print '\n', '-'*8, '\n'
        for i in range(0,len(m)):
            print  ' '.join(map('{}'.format, m[i]))
        print '\n', '-'*8, '\n'

    
    def findPath(m, ml, r, avail):
        t=len(avail)
        #print avail
        if t==ml%2:
            return t
        if r==ml:
            return t
        if sum(m[r])==0 or not (r in avail):
            return findPath(m, ml, r+1, avail)


        for i in range(0, ml):
            if (not i in avail) or (m[r][i]==0):
                continue
            
            availCopy=[x for x in avail if (x!=i and x!=r)]
            if len(availCopy)==ml%2:
                return ml%2
            tt=findPath(m, ml, r+1, availCopy)
            if tt==ml%2:
                return tt
            if t>tt:
                t=tt
        return t

    def findNum(m):
        lm=len(m)
        return findPath(m, lm, 0, range(0, lm))
    

    def getMtx(l):
        ll=len(l)

        m=[[0 for i in range(0, ll)] for j in range(0, ll) ]
        for i in range(0, ll):
            for j in range(0, ll):
                if i>j:
                    m[i][j]=1 if everPlaying(l[i], l[j]) else 0
        for i in range(0, ll):
            for j in range(0, ll):
                if i<j:
                    m[i][j]=m[j][i]
                    
        return m

    def sampleMtx(n, rate1):
        from random import random
        m=[[0 for i in range(0, n)] for j in range(0, n) ]
        for i in range(0, n):
            for j in range(0, n):
                if i>j:
                    m[i][j]=1 if random()<rate1 else 0
        for i in range(0, n):
            for j in range(0, n):
                if i<j:
                    m[i][j]=m[j][i]
                    
        return m

    
    def pmtx(m):
        print '\n', '-'*8, '\n'
        for i in range(0,len(m)):
            print  ' '.join(map('{}'.format, m[i]))
        print '\n', '-'*8, '\n'

    m=sampleMtx(50, r1)
    pmtx( m)
    m=sortM(m)
    print 'after sorted'
    pmtx (m)
    l=0
    l=findNum(m)
    
    #print l
    return l
    




    

    l=banana_list
    from random import random
    '''
    l=[1,1]    
    l=[1,7,3,21,13]
    l=[1,7,3,21,13,19]
    
    max=2**28

    x,y=int(random()*max)*4, int(random()*max)*4
    print x,y, everPlaying(x,y)
    return
    '''
    max=2**28
    l = [int(random()*max)*2 for i in range(0, 151)]

    from time import time
    ta=time()
    m=getMtx(l)
    tb=time()
    #pmtx( m)
    m=sortM(m)
    #pmtx( m)
    left=findNum(m)
    tc=time()

    d1=tb-ta
    d2=tc-tb
    if d1> 4:
        print 'matching: ', l
    if d2> 4:
        print 'finding: ', l
    print left
    return left

    print everPlaying(3, 7)
    return

        
    m=[[0,1,0,1],[1,0,0,0],[0,0,0,0],[0,1,1,1]]
    pmtx(m)
    m=sortM(m)
    pmtx(m)

    x,y=1,3
    x,y=2,6
    x,y=262565534, 437096802
    print x, y, everPlaying(x,y)

    
    return


    

n=10**2
print 1
from time import time
from random import random
t=time()
for i in range(0, n):
    #r=random()
    r=0.1
    print i, r
    c= f(0, r)
    if c!=0:
        print c
    
t=time()-t
print (t+0.0)/n
