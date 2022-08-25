
# 1 은 n극, 2는 s극
# 윗부분에 n극 , 아랫부분에 s극

t = 10
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)

    arr3 = []

    for i in range(n):
        arr2 = []
        arr3.append(arr2)
        for j in range(n):
            arr2.append(arr[j][i])
    # print(arr3)

    stack = []
    cnt = 0

    for k in range(n):
        start = 0
        for g in range(n):
            if arr3[k][start] == 1:
                stack.append(start)
                for x in range(start, n):
                    if arr3[k][x] == 2:
                        cnt += 1
                        start = x
                        break
                else:
                    start+=1
            else:
                start+=1
            if start>=n:
                break

    print(f'#{tc+1} {cnt}')



