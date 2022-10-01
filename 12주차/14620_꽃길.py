N = int(input())
garden = [list(map(int,input().split())) for _ in range(N)]
mincost = 99999
for a in range(1,N-1):
    for b in range(1,N-1):
        costa = garden[a][b]+garden[a-1][b]+garden[a+1][b]+garden[a][b+1]+garden[a][b-1]
        for c in range(1,N-1):
            for d in range(1,N-1):
                if abs(a-c)+abs(b-d)>2:
                    costb=garden[c][d]+garden[c-1][d]+garden[c+1][d]+garden[c][d+1]+garden[c][d-1]
                    for e in range(1,N-1):
                        for f in range(1,N-1):
                            if abs(a-e)+abs(b-f)>2:
                                if abs(c-e)+abs(d-f)>2:
                                    costc=garden[e][f]+garden[e-1][f]+garden[e+1][f]+garden[e][f+1]+garden[e][f-1]
                                    if costa+costb+costc<mincost:
                                        mincost = costa+costb+costc
print(mincost)