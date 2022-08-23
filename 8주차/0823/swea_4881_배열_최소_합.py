caseNum = int(input())
for i in range(caseNum):
    N = int(input())
    caseList = [list(map(int,input().split())) for _ in range(N)]
    findList = [_ for _ in range(N)]
    sel=[0]*N
    check = [0]*N
    allList=[]
    def perm(dep):
        if dep == N:
            allList.append(sel)
            return
        for k in range(N):
            if not check[k]:
                check[k] = 1
                sel[dep] = findList[k]
                perm(dep+1)
                check[k] = 0
    perm(0)
    print(allList)

# def min_sum(depth, acc, thisa):
#     global a
#     global minS
#     print(id(thisa))
#     #모든 id값이 다 같음
#     #input_set = set(input_set)을 하면 id값이 달라지게 됨
#
#     if acc > minS:
#         return
#
#     if depth == N:
#         if acc < minS:
#             minS = acc
#         return
#
#     arr = mat[depth]
#     for i in range(N):
#         if not check[i]:
#             acc += arr[i]
#             check[i] = 1
#
#             min_sum(depth + 1, acc, a)
#             check[i] = 0
#
# T = int(input())
# global a
# a = {}
#
#
# for tc in range(1, T+1):
#     N = int(input())
#     mat = [list(map(int, input().split())) for _ in range(N)]
#
#     check = [0]*N
#     sel =[0]*N
#     minS = 999999999
#
#     min_sum(0, 0,a)
#
#     print(f'#{tc} {minS}')