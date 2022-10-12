from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
ground = [['#']*(C+2)]
ground += [['#']+list(input())+['#'] for _ in range(R)]
ground += [['#']*(C+2)]
sheep = 0
wolf = 0

for i in range(1, R+1):
    if ground[i] == ['#']*(C+2):
        continue
    for j in range(1, C+1):
        if ground[i][j] != '#':
            Q = deque()
            Q.append((i, j))
            sheep_count = 0
            wolf_count = 0
            while len(Q)>0:
                item = Q.popleft()
                if ground[item[0]][item[1]] == 'o':
                    sheep_count += 1
                elif ground[item[0]][item[1]] == 'v':
                    wolf_count += 1
                ground[item[0]][item[1]] = '#'

                for k in range(4):
                    if ground[item[0]+dr[k]][item[1]+dc[k]] != '#':
                        Q.append((item[0]+dr[k], item[1]+dc[k]))
            if sheep_count > wolf_count:
                sheep += sheep_count
            else:
                wolf += wolf_count

print(sheep, wolf)