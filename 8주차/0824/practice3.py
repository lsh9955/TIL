#BFS 구현
def BFS(G,v,n):
    global orderList
    #방문한 노드를 기록할 리스트 생성
    visited = [0]*(n+1)
    #방문 순서대로 노드를 넣을 큐 생성
    queue = []
    queue.append(v)
    #큐에서 맨 앞의 요소를 빼서 방문하지 않았다면 연결된 다른 하위 노드를 큐에 넣음
    while queue:
        t = queue.pop(0)
        orderList.append(str(t))
        if not visited[t]:
            visited[t] = True
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
#방문한 노드를 순서대로 입력할 리스트
orderList=[]
inputCase = list(map(int,input()))
#inputcase개수에 1을 더한 만큼 빈 리스트를 생성(해당 값을 인덱스로 할당할 것이기 때문)
nodeList = [[] for _ in range(max(inputCase)+1)]
for k in range(len(inputCase)//2):
    #각자 연결된 노드 인덱스를 넣음
    nodeList[inputCase[k*2]].append(inputCase[k*2+1])
    nodeList[inputCase[k*2+1]].append(inputCase[k*2])
BFS(nodeList,1,len(nodeList))
output = []
#노드 리스트에서 중복되는 부분을 제하고 출력
for p in range(len(orderList)-1):
    if orderList[p] ==orderList[p+1]:
        output.append(str(orderList[p]))
        break
    else:
        output.append(str(orderList[p]))
print("-".join(output))
