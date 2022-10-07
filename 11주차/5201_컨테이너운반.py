T = int(input())
for k in range(T):
    N, M = list(map(int, input().split()))
    containerList = list(map(int, input().split()))
    truckList = list(map(int, input().split()))
    containerList.sort()
    truckList.sort()
    allCount = 0
    while len(truckList) > 0:
        thisTruck = truckList.pop()
        for a in range(len(containerList)-1, -1, -1):
            if thisTruck >= containerList[a]:
                allCount += containerList[a]
                containerList[a] = 999
                break
    print(f'#{k+1} {allCount}')
