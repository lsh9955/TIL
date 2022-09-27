T = int(input())
for k in range(T):
    N = int(input())
    bus = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    cj=[int(input()) for _ in range(P)]
    output = [0 for _ in range(P)]
    for a in range(P):
        for b in range(N):
            if bus[b][0]<=cj[a]<=bus[b][1]:
                output[a]+=1
        output[a] = str(output[a])
    print(f'#{k+1} {" ".join(output)}')