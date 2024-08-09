def can_take_shower(n, s, m, intervals):
    intervals.sort(key=lambda x: x[0])
    if intervals[0][0] >= s:
        return True
    for i in range(1, n):
        if intervals[i][0] - intervals[i-1][1] >= s:
            return True
    if m - intervals[-1][1] >= s:
        return True
    return False
t = int(input())
for _ in range(t):
    n, s, m = map(int, input().split())
    intervals = [list(map(int, input().split())) for _ in range(n)]
    if can_take_shower(n, s, m, intervals):
        print("YES")
    else:
        print("NO")
