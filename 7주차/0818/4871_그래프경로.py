caseCount = int(input())
for k in range(caseCount):
    V, E = map(int, input().split())
    adjMatrix = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        startIdx, endIdx = map(int, input().split())
        adjMatrix[startIdx][endIdx] = 1

    start, end = map(int, input().split())
    visited = [start]
    global routeFind
    routeFind = False


    def find(thisVisit, nowStack):
        global routeFind
        for i in range(V+1):
            if adjMatrix[nowStack][i] == 1 and i == end:
                routeFind = True
                break
            elif adjMatrix[nowStack][i] == 1 and i not in thisVisit:
                nowvisit = thisVisit[:]
                nowvisit.append(i)
                find(nowvisit, i)
    find(visited,start)
    print(f'#{k+1} {1 if routeFind else 0}')