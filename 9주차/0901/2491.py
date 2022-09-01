N = int(input())
listN = list(map(int,input().split()))
maxList = []
ascend=0
descend=0
saveNum=0
for k in range(N-1):
    if listN[k]-listN[k+1]==0:
        if ascend !=0:
            ascend+=1
        elif descend !=0:
            descend +=1
        else:
            saveNum+=1
    elif listN[k]-listN[k+1]>0:
        if saveNum !=0:
            if ascend != 0:
                ascend += saveNum
            elif descend != 0:
                descend += saveNum
            saveNum=0
            ascend+=1
            maxList.append(descend)
            descend=0
    else:
        if saveNum !=0:
            if ascend != 0:
                ascend += saveNum
            elif descend != 0:
                descend += saveNum
            saveNum=0
        print(ascend,descend)
        descend+=1
        maxList.append(ascend)
        ascend=0
print(max(maxList)+1)