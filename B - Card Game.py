t = int(input())
while t > 0:
    arr = list(map(int, input().split()))
    win = 0
    if (arr[0] > arr[2] and arr[1] >= arr[3]) or (arr[0] >= arr[2] and arr[1] > arr[3]):
        win += 1
    if (arr[0] > arr[3] and arr[1] >= arr[2]) or (arr[0] >= arr[3] and arr[1] > arr[2]):
        win += 1
    if (arr[1] > arr[2] and arr[0] >= arr[3]) or (arr[1] >= arr[2] and arr[0] > arr[3]):
        win += 1
    if (arr[1] > arr[3] and arr[0] >= arr[2]) or (arr[1] >= arr[3] and arr[0] > arr[2]):
        win += 1
    print(win)
    t -= 1
    
    
    
