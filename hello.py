def MinDiagonals(n,k):
    if k == 0 :
        return 0
    elif k==1:
        return 1    
    else:
        k-=n
        dg = 1
        c= 1
        while k>0:
            k-=n-c
            dg+=1
            if k<=0:
                break
            k-=n-c
            dg+=1
            c+=1
        return dg
t = int(input())
while t>0:
    n,k = map(int, input().split())
    print(MinDiagonals(n,k))
    t-=1