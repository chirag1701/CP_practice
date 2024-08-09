t = int(input())
while t:
    n,k = map(int, input().split())
    ans = 1+(n-1)*k
    print(ans)
    t-=1
