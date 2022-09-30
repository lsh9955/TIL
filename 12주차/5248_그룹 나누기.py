# T = int(input())
# for k in range(T):
#     N,M  = list(map(int,input().split()))
#     teamlist = list(map(int,input().split()))
#     pairlist = [[] for _ in range(N)]
#     count = 0
#     for a in range(len(teamlist)//2):
#         nowIdx = 0
#         while True:
#             if teamlist[a*2] in pairlist[nowIdx]:
#                 pairlist[nowIdx].append(teamlist[a * 2 + 1])
#                 break
#             elif teamlist[a*2+1] in pairlist[nowIdx]:
#                 pairlist[nowIdx].append(teamlist[a * 2])
#                 break
#             elif len(pairlist[nowIdx])!=0:
#                 nowIdx+=1
#             else:
#                 pairlist[nowIdx].append(teamlist[a*2])
#                 pairlist[nowIdx].append(teamlist[a * 2+1])
#                 break
#     print(pairlist)
#     for b in range(len(pairlist)):
#         if len(pairlist[b])>0:
#             count+=1
#     for b in range(1,N+1):
#         if b not in teamlist:
#             count+=1
#     print(f'#{k+1} {count}')

#find_set: x를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])
# x와 y를 포함하는 두 집합을 통합하는 연산
def union(x,y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    L = list(map(int,input().split()))
    #출석번호인덱스까지 parent리스트 만들어주기(0번은 사용안함)
    # 부모를 자기 자신으로 정의
    parent = [i for i in range(N + 1)]

    # 두개씩잘라서 한 쌍마다 union연산 해준다.
    for i in range(0,len(L),2):
        union(L[i],L[i+1])

    result = set()

    for i in range(1, N + 1):
        result.add(find_set(i))

    print("#{} {}".format(tc, len(result)))