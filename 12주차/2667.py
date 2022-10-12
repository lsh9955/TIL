N = int(input())
house = [list(map(int,input())) for _ in range(N)]
houselist = []

def findhouse(idx):
    house[idx[0]][idx[1]]="P"
    d=[0,0,1,-1]
    l=[1,-1,0,0]
    houselist[-1]+=1
    for c in range(4):
        if 0<=idx[0]+d[c]<=N-1 and 0<=idx[1]+l[c]<=N-1:
            if house[idx[0]+d[c]][idx[1]+l[c]] !=0 and house[idx[0]+d[c]][idx[1]+l[c]] !="P":
                findhouse([idx[0]+d[c],idx[1]+l[c]])
for a in range(N):
    for b in range(N):
        if house[a][b]==1:
            houselist.append(0)
            findhouse([a,b])
houselist.sort()
print(len(houselist))
for k in range(len(houselist)):
    print(houselist[k])
