t = int(input())
while t:
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    last_gs = arr[len(arr)-1]
    arr.append(x)
    arr.insert(0,0)
    s = len(arr)
    diff = 0
    diff_var = 0
    for i in range(1,s-1):
        diff_var = arr[i]-arr[i-1]
        if diff_var>diff:
            diff= diff_var
    diff_var = 2*(x-last_gs) 
    if diff_var>diff:
        diff = diff_var
    print(diff)
    t-=1


