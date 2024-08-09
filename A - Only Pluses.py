t = int(input())
while t:
    arr = list(map(int,input().split()))
    for i in range(0,5):
        arr.sort()
        arr[0]+=1
    print(arr[0]*arr[1]*arr[2])
    t-=1
