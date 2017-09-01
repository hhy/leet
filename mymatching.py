def f(banana_list):
    def _everPlayingP(a, b, kmax, k=0, hit=[]):
        if a==b:
            return False
        if k>kmax or (a,b) in hit:
            return True
        while (a%2==0) and (b%2==0):
            a, b=a/2, b/2
            
        hit.append((a,b))
        if a>b:
            a,b =b, a
        k+=1
        _everPlayingP(a*2, b-a, kmax, k, hit) 

    def everPlaying(a, b):
        s=a+b
        if s%4!=0:
            return True
        k=0;
        while True:
            if s%2!=0:
                break
            s=s/2
            k+=1
        return _everPlayingP(a, b, k)
        
    def pmtx(m):
        print '\n', '-'*8, '\n'
        for i in range(0,len(m)):
            print  ' '.join(map('{}'.format, m[i]))
        print '\n', '-'*8, '\n'


    def getG(l):
        ll=len(l)

        m=[[0 for i in range(0, ll)] for j in range(0, ll) ]
        for i in range(0, ll):
            for j in range(0, ll):
                if i>j:
                    #m[i][j]=1 if everPlaying(l[i], l[j]) else 0
                    m[i][j]=1 if everPlaying(l[i], l[j]) else 0
        #print( '-get g')                    
        for i in range(0, ll):
            for j in range(0, ll):
                if i<j:
                    m[i][j]=m[j][i]
        def getG(m):
            g={}
            for i in range(0, len(m)):
                v=[]
                for j in range(0, len(m[i])):
                    if m[i][j]==1:
                        v.append(j)
                if len(v)>0:
                    g[i]=v
            return g
        g=getG(m)
        pmtx(m)
        print (g)
        return g

    
    
    print ('*'*19, 'orignal')
    print( banana_list)
    print ('*'*19, 'orignal')
    g=getG(banana_list)
    ma=matching(g)
    print(ma)
    print ('*'*19, 'end')
    return (len(banana_list)-len(ma)*2)

    




def test():
    ls=[]
    with open('mm.in', 'r') as myf:
        for l in myf:
            l=l.strip()
            if len(l)>0:
                l=l[1:-1]
                ls.append(l)
    #print('\n'.join(ls))
    ll=[ list(map(int, ls[i].split(', '))) for i in range(0, len(ls))]
    ll.insert(0, [1,1])
    ll.insert(0,[1,7,3,21,13,19])
    
    
    #for i in range(0, len(ll)):
    for i in range(0, 1):
        le=f(ll[i])

        print(le)
    #return ll
    
            
    
#l=sampleL()

#print(f(l))
test()

    
