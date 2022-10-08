t = int(input())
for tc in range(t):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = [list(map(int, input())) for _ in range(P)]

    # print(bus, bus_stop)

    samsong = [0]*(P+1)
    for i in range(len(bus)):
        for j in range(bus[i][0], bus[i][1]+1):
            samsong[j] += 1

    samsong.pop(0)
    # print(samsong)
    print(f'#{tc+1}', *samsong)