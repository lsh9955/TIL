#경사로는 길이가 x이므로, 최소한 x가 포함되어야 함
#경사로가 설치될 수 있는 경우의 수?
# [높,낮] [낮,높]
# 1. 높낮 높낮 어차피 높이차이가 나므로 통과
# 2. 높낮 낮높 앞의 높낮이 얼마나 차지하느냐가 중요
# 3. 낮높 높낮 높이차이가 나므로 통과
# 4. 낮높 낮높 올라가는 부분이므로 상관없을거 같음
#해당 방향으로 올라가는 것을 두자리수로 표현하면 될거같음
#첫 숫자를 원래 높이로 해서, 그거랑 맞냐 다르냐를 구분하기
#앞서나가는 경우 그 인덱스만큼 나가기
# 예) 2 2 2 3 3 이면 2 23 23 3 3
import copy
T = int(input())
for a in range(T):
    N,X = list(map(int,input().split()))
    mapinfo = [list(map(int,input().split())) for _ in range(N)]
    rowinfo = copy.deepcopy(mapinfo)
    makecount=0
    for b in range(N):
        for c in range(N):

            #뒤가 작은 경우
            #뒤에는 공사된 것이 무조건 있으면 안됨
            if c==N-1:

            if c==N-1:
                if int ( str ( rowinfo[b][c])[0]  ) - int ( str ( rowinfo[b][c - 1])[0]  ) == 1:
                # 인덱스가 0보다 작아지거나, 뒤에 경사로가 있거나, 중간에 높이가 달라지면 break
                    flag = True
                    for d in range ( X ):
                        if rowinfo[b][c-1] != rowinfo[b][c - d-1]:
                            flag = False
                            break
                        if len ( str ( rowinfo[b][c - d-1] ) ) > 1:
                            flag = False
                            break
                    if flag:
                        pass
                    else:
                        break
            elif abs(rowinfo[b][c]-rowinfo[b][c+1])>1:
                break
            elif int(str(rowinfo[b][c])[0])-int(str(rowinfo[b][c+1])[0])==-1:
                #인덱스가 0보다 작아지거나, 뒤에 경사로가 있거나, 중간에 높이가 달라지면 break
                if c-X+1<0:
                    break
                else:
                    flag=True
                    for d in range(X):
                        if rowinfo[b][c] != rowinfo[b][c-d]:
                            flag=False
                            break
                        if len(str(rowinfo[b][c-d]))>1:
                            flag = False
                            break
                    if flag:
                        changenum=rowinfo[b][c]
                        for d in range(X):
                            rowinfo[b][c - d] = changenum*10+changenum
                        c = c + X
                    else:
                        break
            #뒤가 낮은 경우
            elif int(str(rowinfo[b][c])[0])-int(str(rowinfo[b][c+1])[0])==1:
                if c+X>N-1:
                    break
                else:
                    flag=True
                    for d in range(X):

                        if rowinfo[b][c+1] != rowinfo[b][c+d+1]:
                            flag=False
                            break
                        if len(str(rowinfo[b][c+d+1]))>1:
                            flag = False
                            break
                    if flag:
                        changenum = rowinfo[b][c+1]
                        for d in range(X):
                            rowinfo[b][c+d+1] = changenum*10+changenum
                        c=c+X
                    else:
                        break
        else:
            makecount+=1
    print(rowinfo)
    colinfo = copy.deepcopy(mapinfo)
    for c in range(N):
        for b in range(N):

            if b==N-1:
                if int ( str ( colinfo[b][c])[0]  ) - int ( str ( colinfo[b-1][c])[0]  ) == 1:
                # 인덱스가 0보다 작아지거나, 뒤에 경사로가 있거나, 중간에 높이가 달라지면 break
                    flag = True
                    for d in range ( X ):
                        if colinfo[b-1][c] != colinfo[b-d-1][c]:
                            flag = False
                            break
                        if len ( str ( colinfo[b-d-1][c] ) ) > 1:
                            flag = False
                            break
                    if flag:
                        pass
                    else:
                        break
            else:
                if int(str(colinfo[b][c])[0])-int(str(colinfo[b+1][c])[0])==-1:
                    #인덱스가 0보다 작아지거나, 뒤에 경사로가 있거나, 중간에 높이가 달라지면 break
                    if b-X+1<0:
                        break
                    else:
                        flag=True
                        for d in range(X):
                            if colinfo[b][c] != colinfo[b-d][c]:
                                flag=False
                                break
                            if len(str(colinfo[b-d][c]))>1:
                                flag = False
                                break
                        if flag:
                            changenum = colinfo[b][c]
                            for d in range(X):
                                colinfo[b-d][c] = changenum*10+changenum
                            b = b + X
                        else:
                            break
                #뒤가 낮은 경우
                elif int(str(colinfo[b][c])[0])-int(str(colinfo[b+1][c])[0])==1:
                    if b+X>N-1:
                        break
                    else:
                        flag=True
                        for d in range(X):
                            if colinfo[b+1][c] != colinfo[b+d+1][c]:
                                flag=False
                                break
                            if len(str(colinfo[b+d+1][c]))>1:
                                flag = False
                                break
                        if flag:
                            changenum = colinfo[b+1][c]
                            for d in range(X):
                                colinfo[b+d+1][c] = changenum*10+changenum
                            b = b + X
                        else:
                            break
        else:
            makecount+=1
    print(f'#{a+1} {makecount}')
