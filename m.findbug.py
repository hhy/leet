def pmtx(m):
    print '\n', '-'*8, '\n'
    for i in range(0,len(m)):
        print  ' '.join(map('{}'.format, m[i]))
    print '\n', '-'*8, '\n'

def f():
    def findPath(m, ml, r, avail, modu, path=[]):
        #path.sort(lambda x,y: x-y)
        #print('{}#-{}-[{}]'.format(r,len(path), ','.join(path)))
        #print(avail)
        t=len(avail)
        if t==modu:
            return t
        if r==ml:
            return t
        if sum(m[r])==0 or not (r in avail):
            return findPath(m, ml, r+1, avail, modu,  path)

        possibleMin=t-(ml-r)*2+modu
        for i in range(0, ml):
            if (not i in avail) or (m[r][i]==0):
                continue
            
            availCopy=[x for x in avail if (x!=i and x!=r)]
            pathCopy=[x for x in path]
            pathCopy.append('{}.{}'.format(i,r))
            tt=findPath(m, ml, r+1, availCopy, modu, pathCopy)
            if tt<=possibleMin or tt<=modu:
                t=tt
                break

            if t>tt:
                t=tt
        print('-end--{}#-{}-[{}]'.format(r,len(path), ','.join(path)))
        return t

    def findNum(m):
        lm=len(m)
        return findPath(m, lm, 0, range(0, lm), lm%2)

    def getMFromF(fp):
        m=[]
        with open(fp, 'r') as f:
            for l in f:
                l=l.strip()
                m.append(l.split(' '))
        l=len(m)
        m=[[int(m[i][j]) for i in range(l)] for j in range(l)]
        return m

    fp='mm.in.everlooping'
    m=getMFromF(fp)
    pmtx(m)
    findNum(m)

def g():
    m={(0,1):10, (0,2):10, (1,2):2, (1,3):4,(1,4):8,(2,4):9, (3,5):10,
       (4,3):6,(4,5):10}
    s,a,b,c,d,t=0,1,2,3,4,5
    m={(s,a):10, (s,c):8, (a,b):5, (a,c):2, (b,t):7, (c,d):10, (d,b):8, (d,t):10}

    def nn(m):
        mm=dict()
        for v in m:
            if v[1]==0:
                continue
            mm[v]=m[v]
            mm[(v[1], v[0])]=0
        return mm
    
    def setMini(p, nc, nf, orig, t):

        cmin=min(list(map(lambda v: nc[v]-nf[v], p)))
        print('min: ', cmin)
        for v in p:
            #if v[0]!=0 and v[1]!=t:
            if  v in orig:
                nf[v]+=cmin
                nc[(v[1], v[0])]+=cmin
            else:
                nf[(v[1], v[0])]-=cmin
                nc[v]-=cmin
    
    def path(orig, nc, nf, t, s=0, p=[]):
        existPath=False
        if s==t:
            print('- '*20)
            l=[(x, nc[x]) for x in nc if nc[x]!=0]
            l.sort(lambda a,b: a[0][0]-b[0][0])
            print('cap: ',l)
            l=[(x, nf[x]) for x in nc if nc[x]!=0]
            l.sort(lambda a,b: a[0][0]-b[0][0])
            print('flow: ', l)
            print('path: ', p)
            l=[(x, nf[x]) for x in nc if (x[0]==0 or x[1]==t)]
            print ('io', l)
            setMini(p, nc,nf, orig, t)
            return True
        for vv in nc:
            if ((vv[0]!=s)
                or ( vv in p )
                or (nc[vv]-nf[vv]==0)):
                continue
            #print (vv)
            pp=p[:]
            pp.append(vv)
            if path(orig, nc,nf,  t,vv[1], pp):
                return True

        return existPath

        
    nc=nn(m)
    nf=nn(m)
    for v in nf:
        nf[v]=0

    while True:
        print('* '*20)
        if not path(m, nc, nf, 5):
            break

    for v in nf:
        if v[0]==0:
            print(v, nf[v])
        if v[1]==5:
            print(v, nf[v])
    
                
        
g()    
    

