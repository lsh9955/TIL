YSlist=[list(map(str,input())) for _ in range(5)]
sellist = [i+1 for i in range(25)]
#상남자식 조합
Ycount = 0
for a in range(19):
    for b in range(a+1,20):
        for c in range(b+1,21):
            for d in range(c+1,22):
                for e in range(d+1,23):
                    for f in range(e+1,24):
                        for g in range(f+1,25):
                            nowlist=[[a//5,a%5],[b//5,b%5],[c//5,c%5],[d//5,d%5],[e//5,e%5],[f//5,f%5],[g//5,g%5]]
                            Snum = 0
                            for h in range(7):
                                if YSlist[nowlist[h][0]][nowlist[h][1]]=="S":
                                    Snum+=1
                            if Snum>=4:
                                thisl=[0,0,1,-1]
                                thisr=[1,-1,0,0]
                                flag=True
                                for i in range(7):
                                    
                                    for j in range(4):
                                        if 0<=nowlist[i][0]+thisl[j]<=4 and 0<=nowlist[i][1]+thisr[j]<=4:
                                            if [nowlist[i][0]+thisl[j],nowlist[i][1]+thisr[j]] in nowlist:
                                                break
                                    else:
                                        flag=False
                                        break
                                if flag:
                                    Ycount+=1
print(Ycount)

