import copy
N, L = list(map(int,input().split()))
maplist = [list(map(int,input().split())) for _ in range(N)]
rlmap = copy.deepcopy(maplist)
roadcount = 0
for a in range(N):
    road = True
    for b in range(N-1):
        if rlmap[a][b] - rlmap[a][b+1]==1:
            fixroad = rlmap[a][b]-1
            for c in range(L):
                if b+1+c>N-1 or rlmap[a][b+1+c] != fixroad :
                    road = False
                    break
                else:
                    rlmap[a][b+1+c]=rlmap[a][b+1+c]*10
        elif rlmap[a][b]//10 - rlmap[a][b+1]==1:
            fixroad = rlmap[a][b]-1
            for c in range(L):
                if b+1+c>N-1 or rlmap[a][b+1+c] != fixroad :
                    road = False
                    break
                else:
                    rlmap[a][b+1+c]=rlmap[a][b+1+c]*10
        elif rlmap[a][b+1] - rlmap[a][b] ==1:
            fixroad = rlmap[a][b+1]-1
            for c in range(L):
                if b-c<0 or rlmap[a][b-c] != fixroad :
                    road = False
                    break
                else:
                    rlmap[a][b-c]=rlmap[a][b-c]*10
        elif rlmap[a][b] == rlmap[a][b+1] or rlmap[a][b]//10 == rlmap[a][b+1]:
            pass

        else:
            road = False
            break
    if road:
        print(a)
        roadcount+=1
print(rlmap)
btmap = copy.deepcopy(maplist)
for a in range(N):
    road = True
    for b in range(N-1):
        if btmap[b][a] - btmap[b+1][a]==1:
            fixroad = btmap[b+1][a]
            for c in range(L):
                if b+1+c>N-1 or btmap[b+1+c][a] != fixroad :
                    road = False
                    break
                else:
                    btmap[b+1+c][a]=btmap[b+1+c][a]*10
        elif btmap[b][a]//10 - btmap[b+1][a]==1:
            fixroad = btmap[b+1][a]
            for c in range(L):
                if b+1+c>N-1 or btmap[b+1+c][a] != fixroad :
                    road = False
                    break
                else:
                    btmap[b+1+c][a]=btmap[b+1+c][a]*10
        elif btmap[b+1][a] - btmap[b][a] ==1:
            fixroad = btmap[b][a]
            for c in range(L):
                if b-c<0 or btmap[b-c][a] != fixroad :
                    road = False
                    break
                else:
                    btmap[b-c][a]=btmap[b-c][a]*10
        elif btmap[b][a] == btmap[b+1][a] or btmap[b][a]//10 == btmap[b+1][a]:
            pass
        else:
            road = False
            break
    if road:

        roadcount+=1

print(roadcount)