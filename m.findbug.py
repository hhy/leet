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

f()    
    

