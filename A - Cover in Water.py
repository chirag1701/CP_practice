t = int(input())
while t:
    n = int(input())     
    s = input()
    matrix = []
    for seq in s.split("#"):
        matrix.append(seq)
    maxx = max(len(seq) for seq in s.split('#'))
    if maxx>=3:
        print(2)
    else:
        count = 0
        for i in range(0,len(matrix)):
             if len(matrix[i])>0:
                count+=len(matrix[i])
        print(count)
    t-=1

            
