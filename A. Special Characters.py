t = int(input())
while t > 0:
    n = int(input())
    if n % 2 == 0:
        print("YES")
        for i in range(65, 65 + (n // 2)):
            print(chr(i) * 2, end='')
        print()
    else:
        print("NO")
    t -= 1
