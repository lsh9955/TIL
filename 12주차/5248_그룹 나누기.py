#x를 포함하는 집합을 찾음
def findset(x):
    if x==parent[x]:
        return x
    else:
        return findset(parent[x])
# x,y를 포함하는 두 집합을 통합
def union(x,y):
    parent[findset(y)] = findset(x)

T=int(input())
for k in range(1,T+1):
    N,M = map(int,input().split())
    L = list(map(int,input().split()))
    #출석 번호의 인덱스까지 parent리스트를 만들어줌(0은 사용X)
    parent = [i for i in range(N+1)]
    #두 개를 한 쌍으로 union
    for a in range(0,len(L),2):
        union(L[a],L[a+1])

    result = set()

    for b in range(1,N+1):
        result.add(findset(b))

    print(f'#{k} {len(result)}')