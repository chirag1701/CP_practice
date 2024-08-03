t = int(input())
def count_occurence(arr):
    arr1 = [0,0,0,0,0,0,0]
    for i in range(0,len(arr)):
        if arr[i]=='A':
            arr1[0]+=1
        elif arr[i]=='B':
            arr1[1]+=1
        elif arr[i]=='C':
            arr1[2]+=1
        elif arr[i]=='D':
            arr1[3]+=1
        elif arr[i]=='E':
            arr1[4]+=1
        elif arr[i]=='F':
            arr1[5]+=1
        elif arr[i]=='G':
            arr1[6]+=1
        else:
            None
    return arr1
while t:
    n,m = map(int, input().split())
    str = input()
    arr = list(str)
    arr1 = count_occurence(arr)
    count = 0
    for i in range(0,7):
        if arr1[i]<m:
            count+= (m-arr1[i])
    print(count)
    t-=1
