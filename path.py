vv=[[	0	,	1	,	1	,	0	],
         [	0	,	0	,	0	,	1	],
         [	1	,	1	,	0	,	0	],
         [	1	,	1	,	1	,	0	]]
vv=[[0,0,0,0,0,0],
    [1,1,1,1,1,0],
    [0,0,0,0,0,0],
    [0,1,1,1,1,1],
    [0,1,1,1,1,1],
    [0,0,0,0,0,0]]

def getNeighbours(y=0,x=0,inc={}):
    #print ('iii: ', inc, (y+1, x) in inc)
    vs=[ (y+a, x+b)
         for a in [-1,0, 1]
         for b in [-1,0, 1]
         if (y+a, x+b) in inc
         and a+b in [1, -1]
    ]
    return vs

def getAllChange(ymax, xmax, m):
    vs=[(y+a, x+b)
        for y in range(0, ymax)
        for x in range(0, xmax)
        for a in [-1,0, 1]
        for b in [-1,0, 1]
        if 1==1
        and y+a>=0 and y+a<ymax
        and x+b>=0 and x+b<xmax
        and a+b in [-1, 1]
        and m[y][x]==0
        and m[y+a][x+b]==1
        ]
    return vs


def nextRound(v, unved, ved):
    l=v[1]+1
    #print(v)
    vs=getNeighbours(v[0][0], v[0][1], unved)
    #print('neightbourse: ', vs, ', in: ', unved)
    for vn in vs:
        if unved[vn]==-1 or unved[vn]>l:
            unved[vn]=l
        

def sp(vv):
    max=99999999999999
    ymax=len(vv)
    xmax=len(vv[0])

    vs=[(y, x) for y in range(0,ymax) for x in range(0, xmax) if vv[y][x]==0]
    vs=[(x,max) for x in vs]
    unved=dict(vs)
    ved=[]
    unved[(0,0)]=0
    while len(unved)>0:
        v=min(unved.items(), key=lambda x: x[1])
        #print(' start v: ', v)
        if (v[0][0]==(ymax-1)) and (v[0][1]==(xmax-1)):
            pl=unved[v[0]]+1
            #print('shortest: ', pl)
            return pl
        nextRound(v,unved, ved)
        ved.append(v)
        del(unved[v[0]])
        #print('visit: ', ved)
        #print('unvisit: ', unved)

    
def mm(vv):
    ymax=len(vv)
    xmax=len(vv[0])
    pos=set(getAllChange(ymax, xmax, vv))
    l=999999999999
    for p in pos:
        y, x=p
        vv[y][x]=0
        ll=sp(vv)
        if l>ll:
            l=ll
        vv[y][x]=1
    print l
    return l
        

if __name__=='__main__':
    mm(vv)

