t = int(input())
while t:
    p1,p2,p3 = map(int, input().split())
    if (p1+p2+p3)%2!=0:
        print(-1)
    elif p1+p2<p3:
        print(p1+p2)
    elif p1+p2>=p3:
        print((p1+p2+p3)//2)
    else:
        None
    t-=1        
