t = int(input())
def rshift(arr):
       arr_new =[]
       arr_new.insert(0,arr[len(arr)-1])
       for i in range(0,len(arr)-1):
          arr_new.append(arr[i])
       return arr_new
while t:
    n,m = map(int, input().split()) 
    if n==1 and m==1:
        matrixx = int(input())
        print(-1)
    else:
        matrix = []
        for _ in range(n):
           row = list(map(int, input().split()))
           matrix.append(row)
 
        if m==1:
           arr_r = []
           for i in range(0,n):
              arr_r.append(matrix[i][0])
           k=rshift(arr_r) 
           for i in range(0,n):
               print(k[i])
        else:
            for i in range(0,n):
                l=rshift(matrix[i])
                print(' '.join(map(str, l)))
    t-=1
