import sys
input = sys.stdin.readline
R,C = list(map(int,input().split()))
camp = [list(input().strip()) for _ in range(R)]
thislist = []
yangcount = 0
nuckcount  = 0
def findround(idx):
    d=[0,0,1,-1]
    l=[1,-1,0,0]
    if camp[idx[0]][idx[1]]=="v":
        thislist[-1][0]+=1
    elif camp[idx[0]][idx[1]]=="o":
        thislist[-1][1]+=1
    else:
        pass
    camp[idx[0]][idx[1]]="P"
    for c in range(4):
        if 0<=idx[0]+d[c]<=R-1 and 0<=idx[1]+l[c]<=C-1:
            if camp[idx[0]+d[c]][idx[1]+l[c]]!="P" and camp[idx[0]+d[c]][idx[1]+l[c]]!="#":
                findround([idx[0]+d[c],idx[1]+l[c]])

for a in range(R):
    for b in range(C):
        if camp[a][b]!="#" and camp[a][b]!="P":
            thislist.append([0,0])
            findround([a,b])

for a in range(len(thislist)):
    if thislist[a][1]>thislist[a][0]:
        yangcount+=thislist[a][1]
    else:
        nuckcount+=thislist[a][0]
print(f'{yangcount} {nuckcount}')
