t = int(input())
while t>0:
    num =0
    s = input()
    arr = list(s)
    if len(arr)==1:
        if arr[0]!='z':
           arr.append('z')
           
        else:
           arr.append('k') 
    else:
        for i in range(0, len(arr)-1):
           if arr[i]==arr[i+1]:
              if arr[i]=='a':
                arr.insert(i+1,'b')
                break
              else:
                arr.insert(i+1,'a')
                break
           else:
              num+=1
        if num==len(arr)-1:
              if arr[len(arr)-1]!='z':
                 arr.append('z')
              else:
                 arr.append('k')   
    s_new = "".join(arr) 
    print(s_new) 
    t-=1          
