# 세로로 연속된 개수를 가지고 약품을 사이에 넣는 것으로 빠르게 풀 수 없을까?
# A의 연속을 1, B의 연속을 -1로 해서, A약품을 넣으면 +1, B약품을 넣으면 -1로 하는 방식으로...
# 각 행에서의 max값을 구해서, 하면 되지 않을까..?
# 이거 시간초과가 안날수가 있나..?
from collections import deque
import copy
from gettext import find
T = int(input())
for a in range(T):
    D, W, K = list(map(int, input().split()))
    filmlist = [list(map(int, input().split())) for _ in range(D)]
    celllist = [[] for _ in range(W)]
    for b in range(W):
        Anum = 0
        Bnum = 0
        for c in range(D):
            if filmlist[c][b] == 0 and Bnum != 0:
                celllist[b].append(-1*Bnum)
                Bnum = 0
                Anum += 1
            elif filmlist[c][b] == 1 and Anum != 0:
                celllist[b].append(Anum)
                Anum = 0
                Bnum += 1
            else:
                if filmlist[c][b] == 0:
                    Anum += 1
                else:
                    Bnum += 1
        if Anum != 0:
            celllist[b].append(Anum)
        elif Bnum != 0:
            celllist[b].append(-1*Bnum)
    # 처음에 통과하는지 보기
    flag = False
    for f in range(W):
        if max(list(map(abs, celllist[f]))) < K:
            flag = True
            break
    if not flag:
        print(f'#{a+1} 0')
    # else:
    #     # BFS?근데 약품이 두종류인..?
    #     findroute = deque()
    #     for d in range(1, W-1):
    #         #빨간약 or 파란약
    #         for e in range(2):
    #             if e == 0:
    #                 findroute.add([d])
    #             else:
    #                 findroute.add([-1*d])
    #     while findroute():
    #         nowcell = copy.deepcopy(celllist)

    # [첫idx,두번쨰idx...인데, A이면 +, B이면 -]
