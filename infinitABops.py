
def f(n):

    def findSet(a,b, ns): # initial: a=n, b=3*n
        if a*b==0:
            return
        if a%2==0:
            x,y=a/2, a/2+b
            if  (x,y) in ns:
                return
            ns.add((x,y))
            findSet(x,y, ns)
            
        if b%2==0:
            findSet(b, a, ns)
            

    def match(a, b, dic):
        if a==b:
            return False
        if(a<b):
            return match(b, a, dic)
        if (a+b)%4!=0:
            return True
        
        ns=set([])
        n=(a+b)/4
        if not n in dic:
            dic[n]=set()
            pre(n, n*3, dic[n])

        return (a, b) in dic[n]

    def pmtx(m):
        print '\n', '-'*8, '\n'
        for i in range(0,len(m)):
            print  ' '.join(map('{}'.format, m[i]))
        print '\n', '-'*8, '\n'

    def sortM(m):
        l=([(i, sum(m[i])) for i in range(len(m))])
        l.sort(lambda a, b: a[1]-b[1])
        print l
        k=dict([((x,y), m[y][x]) for x in range(0, len(m)) for y in range(0, len(m))])
        mm=[[k[(l[i][0],l[j][0])] for i in range(0, len(m)) ]  for j in range(0, len(m)) ]
        return mm
        
    def sampleMtx(n):
        from random import random
        m=[[(0 if int(random()*1000)%3==0 else 1) for i in range(0,n)] for j in range(0,n)]
        for i in range(0, n):
            for j in range(i+1, n):
                m[i][j]=m[j][i]
                
            m[i][i]=0

                
        pmtx(m)
        m=sortM(m)
        pmtx(m)

        

        
        
    sampleMtx(20)
    def findPath(mtx):
        pass
    #dic={}
    #m=match(10,22,dic)
    #print m
        
        
f(3)
        
        



        
