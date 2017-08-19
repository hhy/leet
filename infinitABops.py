
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
            print ' '.join(map('{}'.format, m[i]))
        print '\n', '-'*8, '\n'
        
    def sampleMtx(n):
        from random import random
        m=[[(0 if int(random()*1000)%3==0 else 1) for i in range(0,n)] for j in range(0,n)]
        for i in range(0, n):
            for j in range(i+1, n):
                m[i][j]=m[j][i]
                
            m[i][i]=0

                
        pmtx(m)
        m.sort(lambda x, y: sum(x)-sum(y))
        pmtx(m)

        

        
        
    sampleMtx(20)
    def findPath(mtx):
        pass
    #dic={}
    #m=match(10,22,dic)
    #print m
        
        
f(3)
        
        



        
