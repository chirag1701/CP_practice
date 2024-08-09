t = int(input())
while t:
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[1]-arr[0]+arr[2]-arr[1])
    t-=1
