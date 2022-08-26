C, R = list(map(int, input().split()))
K = int(input())
r, l, t, b = 0, 0, 0, 0
nowIdx = [1, 1]
nowPerson = 1
count = 0
# 0 0  1 1  2 2  3 3 4 4
if K > C * R:
    print(0)
# for i in range(R-1):
if nowPerson + R-1 >= K:
    nowIdx[1]+=nowPerson-K
    print(nowIdx[0], end=" ")
    print(nowIdx[1])

else:
    nowPerson += R-1
    nowIdx[1] += R-1
    while nowPerson != K:
        # 시작하는 좌표,끝까지 갈 수 있는 좌표값을 제외하고, 더하는 횟수는 R-1이므로 -1을 추가
        if nowPerson +C - 2 - count*2 >= K:
            nowIdx[0] += nowPerson +C - 1 - count*2 - K
            print(nowIdx[0], end=" ")
            print(nowIdx[1])
            break
        else:
            nowPerson +=C - 2 - count*2
            nowIdx[0] +=C - 2 - count*2

        if nowPerson +R - 2 - count*2 >= K:
            nowIdx[1] += nowPerson + R - 1 - count * 2 - K
            print(nowIdx[0], end=" ")
            print(nowIdx[1])
            break
        else:
            nowPerson += R - 2 - count*2
            nowIdx[1] -= 1+R - 2 - count*2

        if nowPerson + C - count*2-3 >= K:
            nowIdx[1] += nowPerson + R - 1 - count * 2 - K
            print(nowIdx[0], end=" ")
            print(nowIdx[1])
            break
        else:
            nowPerson += 1
            nowIdx[1] += 1

            # for a in range(C - 1 - count*2):
        #     if nowPerson == K:
        #         break
        #     nowPerson += 1
        #     nowIdx[0] += 1

        # for a in range(R - 1 - count*2):
        #     if nowPerson == K:
        #         break
        #     nowPerson += 1
        #     nowIdx[1] -= 1

        # for a in range(C - count*2-2):
        #     if nowPerson == K:
        #         break
        #     nowPerson += 1s
        #     nowIdx[0] -= 1

        # for a in range(R  - count*2-2):
        #     if nowPerson == K:
        #         break
        #     nowPerson += 1
        #     nowIdx[1] += 1

        count += 1

    print(nowIdx[0], end=" ")
    print(nowIdx[1])
