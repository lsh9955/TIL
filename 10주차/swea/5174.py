T = int(input())
for k in range(T):
    E,N = list(map(int,input().split()))
    nodeList = list(map(int,input().split()))
    thisNode = [[] for _ in range(E+2)]
    visited = []
    for p in range(E):
        thisNode[nodeList[p*2]].append(nodeList[p*2+1])
    def findRoute(idx):
        nowI = thisNode[idx]
        for i in range(len(nowI)):
            if nowI[i] not in visited:
                visited.append(nowI[i])
                findRoute(nowI[i])
    findRoute(N)
    print(f'#{k+1} {len(visited)+1}')