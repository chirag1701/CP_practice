t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
