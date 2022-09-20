T = int(input())
for k in range(T):
    N,M = list(map(int,input().split()))
    city = [list(map(int,input().split())) for _ in range(N)]
    K = 1
    print(city)
    money = K*K+(K-1)*(K-1)
    rbIdx = [0,0]
    ltIdx = [K,-K]
    maxHouse = [0 for _ in range(11)]
    for f in range(10):
        for a in range(N+2*K):
            for b in range(N+2*K):
                houseNum = 0

                for c in range(K*2-1):
                    blockNum = K*2-1 - abs(K-1-c)*2
                    firIdx = abs(K-1-c)
                    for d in range(blockNum):
                        if [a,b] == [c,firIdx] and a>=0 and a<=N-1 and b>=0 and b<=N-1:
                            if city[a][b] == 1:
                                houseNum+=1
                        firIdx+=1
                if houseNum>maxHouse[K]:
                    maxHouse[K]=houseNum
        if maxHouse[K]*M<money:
            break
        else:
            K+=1
    print(maxHouse)
            