t = int(input())
while t>0 :
    n,a,b = map(int, input().split())
    if b>=a:
        k = min(n, b-a+1) #including b=a ter
        sum_k_terms = k*(b+b-k+1)//2 
        remaining_terms = n-k
        price = (n-k)*a + sum_k_terms
        print(price)
    else:
        price = n*a
        print(price)
    t-=1
