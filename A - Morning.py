t = int(input())
while t:
    str = input()
    arr = list(str)
    arr_new = list(map(int, arr))
    arr_num = [1,2,3,4,5,6,7,8,9,0]
    start = 1
    press = 0
    shift = 0
    for i in range(0,4):
        if i==0:
            start = 1 
        else:
            start = arr_new[i-1]
        if arr_new[i]==start:
            press+=1
        elif arr_new[i]==0 or start == 0:
            adj_diff = 10 - abs((arr_new[i])-(start))
            shift+= adj_diff
            press+=1  
        else:
            adj_diff = abs((arr_new[i])-(start))
            shift+= adj_diff
            press+=1  
    print(press+shift)        
    t-=1
