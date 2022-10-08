t = int(input())
for tc in range(t):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]

    box = [0 for _ in range(N)]
    # print(box)

    for i in range(len(arr)):
        for j in range(arr[i][0]-1, arr[i][1]):
            box[j] = i+1

    print(f'#{tc+1}', *box)