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
if nowPerson + R - 1 >= K:
    nowIdx[1] += K - nowPerson
    print(nowIdx[0], end=" ")
    print(nowIdx[1])

else:
    nowPerson += R - 1
    nowIdx[1] += R - 1

    while nowPerson < K:
        # 시작하는 좌표,끝까지 갈 수 있는 좌표값을 제외하고, 더하는 횟수는 R-1이므로 -1을 추가
        if nowPerson + C - 1 - count * 2 >= K:
            nowIdx[0] += K - nowPerson
            print(nowIdx[0], end=" ")
            print(nowIdx[1])

            break
        else:
            nowPerson += C - 1 - count * 2
            nowIdx[0] += C - 1 - count * 2

        if nowPerson + R - 1 - count * 2 >= K:
            nowIdx[1] -= K - nowPerson
            print(nowIdx[0], end=" ")
            print(nowIdx[1])

            break
        else:
            nowPerson +=  R - 1 - count * 2
            nowIdx[1] -= R - 1 - count * 2

        if nowPerson + C - count * 2 - 2 >= K:
            nowIdx[0] -= K - nowPerson
            print(nowIdx[0], end=" ")
            print(nowIdx[1])
            break
        else:
            nowPerson += C - count * 2 - 2
            nowIdx[0] -=C - count * 2 - 2

        if nowPerson + R - count * 2 - 2 >= K:
            nowIdx[1] += K - nowPerson
            print(nowIdx[0], end=" ")
            print(nowIdx[1])
            break
        else:
            nowPerson += R - count * 2 - 2
            nowIdx[1] += R - count * 2 - 2
        count += 1
