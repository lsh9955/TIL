T = int(input())
for k in range(T):
    N,M,L = list(map(int,input().split()))
    nodeList = [0 for _ in range(N+1)]
    for i in range(M):
        nowIdx,nowNum = list(map(int,input().split()))
        nodeList[nowIdx] = nowNum
    for p in range(N,-1,-1):
        thisIdx = p
        thisNum = nodeList[thisIdx]
        thisIdx = thisIdx//2
        nodeList[thisIdx]+=thisNum
    print(f'#{k+1} {nodeList[L]}')
