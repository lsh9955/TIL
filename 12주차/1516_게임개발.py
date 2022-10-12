# # 정점의 갯수, 간선의 갯수
# vertexes,edges=map(int,input().split())
# # 인접리스트
# adj_list=[[] for _ in range(vertexes+1)]

# # 연결리스트 작성
# for _ in range(edges):
#     i,j=map(int,input().split())
#     adj_list[i].append(j)

# topology_sort=[] # 위상정렬 결과를 저장하는 스택
# nvisit=[1]*(vertexes+1) #방문 확인용.방문은 0 미방문은 1

# # 위상정렬 1 사이클 함수
# def Topology_Sort_DFS(x):
#     stack=[] #깊이 우선 탐색용 스택
#     stack.append((0,x)) # (지나온 길,시작점) 넣기
#     while stack:
#         isRoute,curr=stack.pop() #스택에 저장된 최근 길
#         if isRoute:topology_sort.append(curr) # 지나온 길이면 위상정렬결과에 넣는다.
#         if nvisit[curr]: # t에 방문한 적이 없으면
#             nvisit[curr]=0 # t에 방문하고
#             stack.append((1,curr)) # 현재 지나온 길임을 표시하고 다시 넣는다.
#             #t와 연결된 곳 중 방문하지 않은 곳만 아직 지나온 길이 아님을 표시하고 모두 스택에 넣는다.
#             for i in adj_list[curr]:
#                 if nvisit[i]:
#                     stack.append((0,i))

# # 모든 점에 대해서 위상정렬 사이클을 돌림
# for i in range(1,vertexes+1):
#     if nvisit[i]:Topology_Sort_DFS(i)

# print(topology_sort[::-1])


N = int(input())
buildinglist = [list(map(int,input().split())) for _ in range(N)]

bdict = {}
global countnum
global countlist
 
countlist=[]
def findsum(idxlist):
    global countnum
    if idxlist!=[]:
        for e in range(len(idxlist)):
            if idxlist[e] not in countlist:
                countlist.append(idxlist[e])
                countnum+=timelist[idxlist[e]-1]
                findsum(bdict[idxlist[e]])




for a in range(N):
    bdict[a+1]=buildinglist[a][1:-1]
timelist = [p[0] for p in buildinglist]


for b in range(N):
    countnum=0
    countlist=[]
    if  bdict[b+1]==[]:
        print(timelist[b])
    else:
        countnum+=timelist[b]
        countlist.append(b+1)
        findsum(bdict[b+1])
        print(countnum)
