t = int(input())
for tc in range(t):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]
    end = 0
    ans = 0
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 3:
                end = (i, j)
    visited = []
    stack = [end]  #stack = [(i,j)]
    while stack: #stack이 빌때까지 while 문을 돌아라!
        print(stack)
        (x, y) = stack.pop(0)
        if x+1 < n and miro[x+1][y] == 2:  #아래
            ans = 1
            break
        elif x+1 < n and miro[x+1][y] == 0 and (x+1, y) not in visited:
            visited.append((x+1, y))
            stack.append((x+1, y))
        if y+1 < n and miro[x][y+1] == 2: #오른쪽
            ans = 1
            break
        elif y+1 < n and miro[x][y+1] == 0 and (x, y+1) not in visited:
            visited.append((x, y+1))
            stack.append((x, y+1))
        if y-1 >= 0 and miro[x][y-1] == 2:  #왼쪽
            ans = 1
            break
        elif y-1 >= 0 and miro[x][y-1] == 0 and (x, y-1) not in visited:
            visited.append((x, y-1))
            stack.append((x, y-1))
        if x-1 >= 0 and miro[x-1][y] == 2: #위
            ans = 1
            break
        elif x-1 >= 0 and miro[x-1][y] == 0 and (x-1, y) not in visited:
            visited.append((x-1, y))
            stack.append((x-1, y))
    print(f'#{tc+1} {ans}')