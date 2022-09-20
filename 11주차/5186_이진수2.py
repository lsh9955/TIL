T = int(input())
for k in range(T):
    N=float(input())
    j=-1
    findSc = [0 for _ in range(12)]
    for p in range(12):
        if N>=2**j:
            N = N-2**j
            findSc[j]=1
        j-=1
    if N != 0:
        print(f'#{k+1} overflow')
    else:
        print(f'#{k+1}', end=" ")
        findIdx=0
        for d in range(12):
            if findSc[d] ==1:
                findIdx=d
                break
        for d in range(11,findIdx-1,-1):
            print(findSc[d], end="")
        print()