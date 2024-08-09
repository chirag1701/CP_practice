N = int(input())
arr = list(map(int, input().split()))
for i in range(0,len(arr)):
    if arr[i]<0:
        arr[i] = abs(arr[i])
min = min(arr)
print(min)
