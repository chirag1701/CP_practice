t = int(input())
while t:
    n,k = map(int, input().split())
    arr = list(map(int,input().split()))
    if k==1:
        count = 0
        for i in range(0,n-1):
            if arr[i+1]>=arr[i]:
                count+=1
        if count==n-1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    t-=1
