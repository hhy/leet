# find +1 -1 /2 ops minimal to 1 from int
def f(n=9):
    def divDecS(s):
        carry, ss=0, ''
        for i in range(0, len(s)):
            c=carry*10+int(s[i])
            carry=c % 2;
            d=c/2
            if len(ss)!=0 or d!=0:
                ss+=str(d)
        return (ss, carry)

    def decS2BinS(s):
        ss=''
        while True:
            s, b=divDecS(s)
            ss=str(b)+ss
            if s=='':
                return ss
            
    def doubleDecSplus(s, a):
        ss=''
        carry=a
        for i in range(0, len(s)):
            i=-1-i;
            a=int(s[i])*2+carry
            carry=a/10
            ss=str(a%10)+ss
        if carry>=1:
            ss=str(carry)+ss
        return ss
            
    def binS2DecS(bs):
        decS=''
        for i in range(0, len(bs)):
            decS=doubleDecSplus(decS, int(bs[i]))
        return decS

    def count(s):
        s=decS2BinS(s)
        l=list(s)
        c=0
        cc=0
        while len(l)>0:
            k=list.pop(l)
            if k=='1':
                cc+=1
                continue

            if cc==0:
                c+=1
            elif cc==1:
                c+=3
            else:
                c+=(cc+1)
                l.append('1')
            cc=0
        if cc==1:
            pass
        if cc==2:
            c+=2
        if cc>2:
            c+=cc+1
        return c

    
    def cnt(s):
        m=int(s)
        ms=[m]
        s=decS2BinS(s)
        print(s)
        l=list(s)
        c=0
        cc=0
        while len(l)>0:
            k=list.pop(l)
            if k=='1':
                cc+=1
                continue

            if cc==0:
                m/=2
                ms.append(m)
                c+=1
            elif cc==1:
                m-=1
                ms.append(m)
                m/=2
                ms.append(m)
                m/=2
                ms.append(m)
                c+=3
            else:
                m+=1
                ms.append(m)
                for i in range(0, cc):
                    m/=2
                    ms.append(m)
                c+=(cc+1)
                l.append('1')
            cc=0
        print('*********m = {}, 1: {}, total: {}'.format(m, cc, c))
        if cc==1:
            pass
        if cc==2:
            m-=1
            ms.append(m)
            ms.append(m/2)
            c+=2
        if cc>2:
            m+=1
            ms.append(m)
            for i in range(0, cc):
                m/=2
                ms.append(m)            

            c+=cc+1
        print '--------------', ms
        print '************* ', map(lambda x: decS2BinS(str(x)), ms), "\n"
        
        return c


    def t():
        l= ['4', '15', '11', '13', '61', '64', '5046']
        #l=['19']
        n=map(cnt, l)
        m=map(count, l)
        b=map(lambda x: bin(int(x)), l)
        print l
        print b
        print m
        print n
        return
        
        ii=[4,5,6,7,34,87]
        iis=map(str, ii)
        print iis
        jjs=map(decS2BinS, iis)
        print jjs
        dds=map(binS2DecS, jjs)
        print dds

        iis=[(2,1), (3,8), (232, 9), (2210, 8), (2325, 2), (223, 4)]
        print(iis)
        ii=[]
        for (x,y) in iis:
             ii.append(doubleDecSplus(str(x), y))
        print(ii)

        ii=[x[0]*2+x[1] for x in iis]
        
        print (ii)

        
        
        
    t()
        

if __name__=='__main__':
    f()

    
