t = int(input())
while t>0:
    n,a,b = map(int, input().split())
    if n%2==0:
       if b>2*a:
          print(n*a)
       else:
          print(b*(n//2))
    else:
       if b>2*a:
          print(n*a)
       else:
          print(b*(n//2)+a)      
    t-=1           
