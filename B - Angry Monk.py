t = int(input())
while t>0:
    count = 0
    n,k =map(int,input().split())
    str = input()
    arr = sorted(list(map(int, str.split())))
    for i in range(0,len(arr)-1):
        if arr[i]==1:
            count+=1
        else:
            count+=(2*arr[i]-1)
    print(count)
    t-=1
