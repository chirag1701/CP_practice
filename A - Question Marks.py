t = int(input())
while t:
    n = int(input())
    str = input()
    arr = list(str)
    countA = 0
    countB = 0
    countC = 0
    countD = 0
    countQ = 0
    for i in range(0,4*n):
        if arr[i]=="A":
            countA+=1
        elif arr[i]=="B":
            countB+=1
        elif arr[i]=="C":
            countC+=1
        elif arr[i]=="D":
            countD+=1
        else:
            countQ+=1
    correct = 0
    if countA>=n:
        correct+=n
    else:
        correct+=countA
    if countB>=n:
        correct+=n
    else:
        correct+=countB
    if countC>=n:
        correct+=n
    else:
        correct+=countC
    if countD>=n:
        correct+=n
    else:
        correct+=countD
    print(correct)
    t-=1

