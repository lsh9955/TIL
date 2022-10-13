
#모든 경우의 수 구하기
#위치+상하좌우[0,1,2,3]
T = int(input())
for a in range(T):
    N = int(input())
    pinball = [list(map(int,input().split())) for _ in range(N)]
    white = []
    for b in range(N):
        for c in range(N):
            if pinball[b][c]>=6:
                white.append([pinball[b][c],b,c])
    global maxcount
    maxcount = []
    def findroute(idx,dir,count,firidx,samecount):

        global maxcount
        #블랙홀, 혹은 원래 idx면 break
        #벽에 부딪힐 경우, 블록에 부딪힐 경우, 웜홀에 빠질 경우,제자리로 돌아올 경우
        if samecount>5:
            maxcount.append(-1)
        elif dir==0:

            #제자리로 돌아올 경우 추가
            if idx[0]-1==-1:
                findroute(idx,1,count+1,firidx,samecount+1)
            elif [idx[0]-1,idx[1]]==firidx:
                maxcount.append(count)
            elif pinball[idx[0]-1][idx[1]]==1 or pinball[idx[0]-1][idx[1]]==4 or pinball[idx[0]-1][idx[1]]==5:
                findroute ( idx, 1, count + 1,firidx,samecount+1 )
            elif pinball[idx[0]-1][idx[1]]==2:
                findroute ( [idx[0]-1,idx[1]], 3, count + 1,firidx,0 )
            elif pinball[idx[0]-1][idx[1]]==3:
                findroute ( [idx[0]-1,idx[1]], 2, count + 1,firidx,0 )
            elif pinball[idx[0]-1][idx[1]]==-1:
                maxcount.append ( count )
            elif pinball[idx[0]-1][idx[1]]>=6:
                for d in range(len(white)):
                    if white[d][0]== pinball[idx[0]-1][idx[1]] and white[d][1:] !=[idx[0]-1,idx[1]]:
                        findroute ( [white[d][1],white[d][2]], 0, count,firidx,0)
                        break
            else:
                findroute ( [idx[0] - 1, idx[1]], 0, count , firidx, 0 )
        elif dir==1:
            # 제자리로 돌아올 경우 추가
            if idx[0]+1 == N:
                findroute ( idx, 0, count + 1 ,firidx,samecount+1)
            elif [idx[0]+1,idx[1]]==firidx:
                maxcount.append(count)
            elif pinball[idx[0]+1][idx[1]]==2 and pinball[idx[0]+1][idx[1]]==3 and pinball[idx[0]+1][idx[1]]==5:
                findroute ( idx, 0, count + 1 ,firidx,samecount+1)
            elif pinball[idx[0]+1][idx[1]]==1:
                findroute ( [idx[0] + 1, idx[1]], 3, count + 1,firidx,0 )
            elif pinball[idx[0]+1][idx[1]]==4:
                findroute ( [idx[0] + 1, idx[1]], 2, count + 1 ,firidx,0)
            elif pinball[idx[0]+1][idx[1]]==-1:
                maxcount.append(count)
            elif pinball[idx[0]+1][idx[1]]>=6:
                for d in range(len(white)):
                    if white[d][0]== pinball[idx[0]+1][idx[1]] and white[d][1:] !=[idx[0]+1,idx[1]]:
                        findroute ( [white[d][1],white[d][2]], 1, count,firidx,0)
                        break
            else:
                findroute ( [idx[0] + 1, idx[1]], 1, count , firidx, 0 )

        elif dir==2:
            # 제자리로 돌아올 경우 추가
            if idx[1]-1 == -1:
                findroute(idx,3,count+1,firidx,samecount+1)
            elif [idx[0],idx[1]-1]==firidx:
                maxcount.append(count)
            elif pinball[idx[0]][idx[1]-1]==3 or pinball[idx[0]][idx[1]-1]==4 or pinball[idx[0]][idx[1]-1]==5:
                findroute ( idx, 3, count + 1 ,firidx,samecount+1)
            elif pinball[idx[0]][idx[1]-1]==1:
                findroute ( [idx[0],idx[1]-1], 0, count + 1 ,firidx,0)
            elif pinball[idx[0]][idx[1]-1]==2:
                findroute ( [idx[0],idx[1]-1], 1, count + 1, firidx ,0)
            elif pinball[idx[0]][idx[1]-1]==-1:
                maxcount.append(count)
            elif pinball[idx[0]][idx[1]-1]>=6:
                for d in range(len(white)):
                    if white[d][0]== pinball[idx[0]][idx[1]-1] and white[d][1:] !=[idx[0],idx[1]-1]:
                        findroute ( [white[d][1],white[d][2]], 2, count, firidx,0)
                        break
            else:
                findroute ( [idx[0], idx[1] - 1], 2, count , firidx, 0 )
        elif dir==3:
            # 제자리로 돌아올 경우 추가
            if idx[1]+1 ==N:
                findroute ( idx, 2, count + 1, firidx,samecount+1 )
            elif [idx[0],idx[1]+1]==firidx:
                maxcount.append(count)
            elif pinball[idx[0]][idx[1]+1]==1 or pinball[idx[0]][idx[1]+1]==2 or pinball[idx[0]][idx[1]+1]==5:
                findroute ( idx, 2, count + 1, firidx ,samecount+1)
            elif pinball[idx[0]][idx[1]+1]==3:
                findroute([idx[0],idx[1]+1],1,count+1, firidx,0)
            elif pinball[idx[0]][idx[1]+1]==4:
                findroute([idx[0],idx[1]+1],0,count+1, firidx,0)
            elif pinball[idx[0]][idx[1]+1]==-1:
                maxcount.append(count)
            elif pinball[idx[0]][idx[1]+1]>=6:
                for d in range(len(white)):
                    if white[d][0]== pinball[idx[0]][idx[1]+1] and white[d][1:] !=[idx[0],idx[1]+1]:
                        findroute ( [white[d][1],white[d][2]], 3, count, firidx,0)
                        break
            else:
                findroute ( [idx[0], idx[1] + 1], 3, count , firidx, 0 )


    for f in range(N):
        for g in range(N):
            if pinball[f][g]==0:
                findroute ( [f,g], 0, 0,[f,g],0)
                findroute ( [f, g], 1, 0, [f, g],0 )
                findroute ( [f, g], 2, 0, [f, g],0 )
                findroute ( [f, g], 3, 0, [f, g],0 )

    print(f'#{a+1} {max(maxcount)}')