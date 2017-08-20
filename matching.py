
def f(banana_list, sol=False):

    def findSet(a,b, ns): # initial: a=n, b=3*n
        if a*b==0:
            return
        if a%2==0:
            x,y=a/2, a/2+b
            if  (x,y) in ns:
                return
            ns.append((x,y))
            findSet(x,y, ns)
            
        if b%2==0:
            findSet(b, a, ns)
            

    def match(a, b, dic={}):
        if a==b:
            return False
        
        if (a+b)%4!=0:
            return True

        if(a>b):
            return match(b, a, dic)
        
        n=(a+b)/4
        if  n in dic:
            return (a,b) in dic[n]
        else:
            dic[n]=[]
        
        findSet(n, n*3, dic[n])
        return (a, b) in dic[n]


    def sortM(m):
        l=([(i, sum(m[i])) for i in range(len(m))])
        l.sort(lambda a, b: a[1]-b[1])
        #print l
        k=dict([((x,y), m[y][x]) for x in range(0, len(m)) for y in range(0, len(m))])
        mm=[[k[(l[i][0],l[j][0])] for i in range(0, len(m)) ]  for j in range(0, len(m)) ]
        return mm

        
    def findPath(m, ml=-1, r=0, avail=None):
        if ml==-1:
            ml=len(m)
        if avail==None:
            avail=range(0, ml)
        if r==ml:
            return 0
        if sum(m[r])==0:
            return findPath(m, ml, r+1, avail)
        t=0

        for i in range(0, ml):
            if (not i in avail) or (m[r][i]==0):
                continue
            
            availCopy=[x for x in avail if x!=i]
            tt=findPath(m, ml, r+1, avail)
            if tt==(ml-r-1):
                t=tt+1
                #print 'optimized!!!'
                break
            if t<tt+1:
                t=tt+1
        return t

    def getMtx(l):
        #dic={}
        ll=len(l)
        m=[[1 if match(l[i], l[j]) else 0 for i in range(0, ll)] for j in range(0, ll)]
        return m

    
    m=getMtx(banana_list)
    m=sortM(m)
    #lmax=findPath(m)
    #return len(m)-lmax

    def pmtx(m):
        print '\n', '-'*8, '\n'
        for i in range(0,len(m)):
            print  ' '.join(map('{}'.format, m[i]))
        print '\n', '-'*8, '\n'
    
    def sampleMtx(n, k=(19,1)):
        from random import random
        m=[[(0 if int(random()*1000)%(k[0])<=(k[1]) else 1) for i in range(0,n)] for j in range(0,n)]
        for i in range(0, n):
            for j in range(i+1, n):
                m[i][j]=m[j][i]
                
            m[i][i]=0

        l=[1,1]
        l=[1,7,3,21,13,19]
        from random import random
        l=[int(random()* (2**30)) for i in range(0, n)]
        l=[1,7,11]
        #m=getMtx(l)
        

        from time import time
        
        t=time()
        m=sortM(m)
        pmtx(m)
        maxL=findPath(m)
        print maxL
        tt=time()
        print 't0: {}, t1:{}, total: {}'.format( t, tt, tt-t)
        return

    
        '''t=time()
        pmtx(m)
        maxL=findPath(m)
        print maxL 
        print time()-t

        print 'left: ', len(m)-maxL
        '''

    print match(7, 1), match(1,7)
    sampleMtx(80, (99,97))
    return

    for k in range(2, 7):
        print '*'*8, k, '*'*8
        sampleMtx(9, k)

l=[1,1]    
l=[1,7,3,21,13,19]    
print f(l)
        
        



        
