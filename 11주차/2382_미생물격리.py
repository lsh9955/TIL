import copy
T = int(input())
for k in range(T):
    N,M,K = list(map(int,input().split()))
    germList = []
    for a in range(K):
        y,x,thisNum,dir= list(map(int,input().split()))
        germList.append([y,x,thisNum,dir])
    for b in range(M):
        timeList = []
        idxDic = {}
        for c in range(len(germList)):
            tdir = germList[c][3]
            if tdir == 1:
                germList[c][0]-=1
            elif tdir == 2:
                germList[c][0]+=1
            elif tdir == 3:
                germList[c][1]-=1
            elif tdir == 4:
                germList[c][1]+=1

            yId= germList[c][0]
            xId= germList[c][1]
            if yId==0:
                germList[c][2]=germList[c][2]//2
                germList[c][3]=2
            elif xId==0:
                germList[c][2]=germList[c][2]//2
                germList[c][3]=4
            elif yId==N-1:
                germList[c][2]=germList[c][2]//2
                germList[c][3]=1
            elif xId==N-1:
                germList[c][2]=germList[c][2]//2
                germList[c][3]=3
            if germList[c][2] != 0:
                if f'{yId} {xId}' in idxDic:
                    idxDic[f'{yId} {xId}'].append([germList[c][2],germList[c][3]])
                else:
                    idxDic[f'{yId} {xId}']=[[germList[c][2],germList[c][3]]]
        thisTlist = []
        for d in idxDic:
            if len(idxDic[d])>1:
                idxDic[d].sort(key=lambda a:a[0])
                nowArr = idxDic[d]
                print(idxDic)
                thisSum =0
                for g in range(len(nowArr)-1):
                    thisSum+=nowArr[g][0]
                thisdiList = d.split()
                thisDir = [int(thisdiList[0]),int(thisdiList[1]),thisSum,nowArr[-1][1]]
                thisTlist.append(thisDir)
                idxDic[d] = thisDir
            else:
                thisdiList = d.split()
                thisTlist.append([int(thisdiList[0]),int(thisdiList[1]),idxDic[d][0][0],idxDic[d][0][1]])
                    
 
            

        germList =  copy.deepcopy(thisTlist)  
    totalGerm = 0
    for e in range(len(germList)):
        totalGerm += germList[e][2]
    print(f'#{k+1} {totalGerm}')

