t = int(input())
while t:
    a, b = map(int, input().split())
    if b < -1:
        print("NO")
    else:
        print("YES")
    t -= 1
