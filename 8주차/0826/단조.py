caseNum =int(input())
for k in range(caseNum):
    N = int(input())
    numList = list(map(int,input().split()))
    ascendList = []
    for a in range(N):
        for b in range(a,N):
            if a!=b:
                targetNum = numList[a]*numList[b]
                divideNum = []
                while targetNum>0:
                    if targetNum>=10:
                        divideNum.append(targetNum%10)
                        targetNum=targetNum//10
                    else:
                        divideNum.append(targetNum)
                        break
                divideNum.reverse()

                flag = True
                if numList[a]*numList[b]<10:
                    ascendList.append(numList[a]*numList[b])
                for p in range(len(divideNum)-1):
                    if divideNum[p]>divideNum[p+1]:
                        flag=False
                        break
                if flag:
                    ascendList.append(numList[a]*numList[b])
    ascendList.sort()
    if len(ascendList)==0:
        print(f"#{k+1} -1")
    else:
        print(f"#{k+1} {ascendList[-1]}")