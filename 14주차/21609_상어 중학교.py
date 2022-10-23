#블록
#일반 블록이 하나는 있어야 함
#색이 모두 같아야 함
#검은색 X, 무지개 O
#2개보다 커야 함
#모두 붙어 있어야 함
#블록 기준
#무지개 제외 행 번호가 가장 작은
#같다면 열 번호가 가장 작은

#가장 큰 블록그룹을 찾음
#블록 그룹이 여러개면 무지개가 가장 많은 그룹
#찾을 때는 기준 행,열이 가장 큰 것을 찾음



# 인접 블록 찾아 블록 크기, 무지개크기, 블록좌표 출력
import copy
def findroute(a,b, color):
    blocklist = []
    blocklist.append([a,b])
    dc = [-1, 0, 1, 0]
    dr = [0, 1, 0, -1]
    blockcount, rainbowcount = 1,0
    normalblocks, rainbows  = [[a,b]],[]

    while len(blocklist)>0:
        a,b = blocklist.pop(0)
        for d in range(4):
            if 0<=a+dc[d]<N-1 and 0<=b+dr[d]<N-1 and visit[a+dc[d]][b+dr[d]]==0  and colorlist[a+dc[d]][b+dr[d]]==color:
                visit[a+dc[d]][b+dr[d]]=1
                blocklist.append([a+dc[d],b+dr[d]])
                blockcount+=1
                normalblocks.append([a+dc[d],b+dr[d]])
            elif 0<=a+dc[d]<N-1 and 0<=b+dr[d]<N-1 and visit[a+dc[d]][b+dr[d]]==0 and colorlist[a+dc[d]][b+dr[d]]==0:
                visit[a+dc[d]][b+dr[d]]=1
                blocklist.append([a+dc[d],b+dr[d]])
                blockcount+=1
                rainbowcount+=1
                rainbows.append([a+dc[d],b+dr[d]])
    for e,f in rainbows:
        visit[e][f]=0
    return [blockcount,rainbowcount,normalblocks+rainbows]


# 블록 제거
def remove(block):
    for a,b in block:
        colorlist[a][b] = -9999

def gravity():
    global colorlist
    for i in range(N - 2, -1, -1):
        for j in range(N):
            # -1이 아니면 아래로 다운
            if colorlist[i][j] > -1:
                r = i
                while True:
                    # -9999이면 아래로
                    if 0 <= r + 1 < N and colorlist[r + 1][j] == -9999:
                        colorlist[r + 1][j] = colorlist[r][j]
                        colorlist[r][j] = -9999
                        r += 1
                    else:
                        break


# 반시계 회전
def rotation():
    global colorlist
    thiscolorlist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            thiscolorlist[N - 1 - j][i] = colorlist[i][j]
    return thiscolorlist



N, M = map(int, input().split())
global colorlist
colorlist = [list(map(int, input().split())) for _ in range(N)]

score = 0

while True:
    # 크기 가장 큰 블록 찾기
    visit = [[0] * N for _ in range(N)]
    blocks = []
    for i in range(N):
        for j in range(N):
            # 일반 블록이면서 방문 안했으면 인접한 블록 찾기
            if colorlist[i][j] > 0 and not visit[i][j]:
                visit[i][j] = 1

                # [블록크기, 무지개블록 개수, 블록좌표]
                blockinfo = findroute(i, j, colorlist[i][j])

                if blockinfo[0] >= 2:
                    blocks.append(blockinfo)
    blocks.sort(reverse=True)

    # 블록제거->점수더하기
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0] ** 2


    gravity()

    colorlist = rotation()

    gravity()
    print(colorlist)

print(score)