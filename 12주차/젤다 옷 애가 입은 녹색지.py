while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(N)]
    rupee = cave[0][0]
    nowidx = [0,0]
    while True:
        if 0<=nowidx[0]<=N-2 and


