T = int(input())
for k in range(T):
    N = int(input())
    factory=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    fac_list = [list(map(int,input().split())) for _ in range(N)]
    totallist = []
    count = 0
    alreadyinput = []
    for a in range(len(fac_list)):
        for b in range(len(fac_list[a])):
            totallist.append([fac_list[a][b],factory[b],a+1])
    totallist.sort(key=lambda x:x[0])
    print(totallist)
    for c in range(len(totallist)):
        if (totallist[c][1] not in alreadyinput) and (totallist[c][2] not in alreadyinput):
            count+=totallist[c][0]
            alreadyinput.append(totallist[c][1])
            alreadyinput.append(totallist[c][2])
        print(alreadyinput)
        if len(totallist)==N*2:
            break
    print(f'#{k+1} {count}')
