T = int(input())
for k in range(T):
    inputList = list(map(int,input().split()))
    N,statList = inputList[0], inputList[1:]+[0]
    maxNum=0
    nowIdx=N-1
    count =0
    while nowIdx>0:
        for a in range(nowIdx-1,-1,-1):
            if nowIdx-a<=statList[a]:
                maxNum=a
        nowIdx=maxNum
        count+=1
        if maxNum<=0:
            break
    print(f'#{k+1} {count-1}')
