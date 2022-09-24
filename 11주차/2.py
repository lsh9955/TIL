def solution(cap, n, deliveries, pickups):
    allDeliver = sum(deliveries)
    allPick = sum(pickups)
    disTance = 0
    while len(deliveries)>0 and len(pickups)>0:
        if n==0:
            break
        while deliveries[-1]==0 and pickups[-1]==0:
            deliveries.pop()
            pickups.pop()
            n-=1
            if n==0:
                break
        if n==0:
            break
        disTance+=n
        willDeliver = [0,0]
        willD = 0
        for k in range(n - 1, -1, -1):
            if willD+deliveries[k]>cap:
                willD = cap
                break
            else:
                willD+=deliveries[k]
        willDeliver=[willD,0]
        for k in range(n - 1, -1, -1):
            if deliveries[k]>willDeliver[0]:
                deliveries[k]-=willDeliver[0]
                willDeliver[0]=0
            else:
                willDeliver[0]-=deliveries[k]
                deliveries[k]=0
            if sum(willDeliver)+pickups[k]<=cap:
                willDeliver[1]+=pickups[k]
                pickups[k]=0
            else:
                if cap-sum(willDeliver)>0:
                    thisab = cap-sum(willDeliver)
                    pickups[k]-=thisab
                    willDeliver[1]+= thisab
                else:
                    break
            # print(willDeliver)
            # if sum(willDeliver)+deliveries[k]+pickups[k]<=cap:
            #     willDeliver[0]+=deliveries[k]
            #     willDeliver[1]+=pickups[k]
            #     deliveries[k]=0
            #     pickups[k]=0
            #
            # elif sum(willDeliver)+deliveries[k]+pickups[k]>cap:
            #     if sum(willDeliver)+deliveries[k]<cap:
            #         willDeliver[0] += deliveries[k]
            #         willMin = cap-(sum(willDeliver)+deliveries[k])
            #         deliveries[k]=0
            #         willDeliver[1]+=willMin
            #         pickups[k]-=willMin
            #
            #     elif sum(willDeliver)+deliveries[k]>cap:
            #         if cap-sum(willDeliver)>0:
            #             deliveries[k] -= cap - sum(willDeliver)
            #             willDeliver[0]+=cap-sum(willDeliver)
            #
            #         else:
            #             if willDeliver[1]+pickups[k]<=cap:
            #                 willDeliver[1]+=pickups[k]
            #                 pickups[k]=0
            #             else:
            #                 pickups[k]-=cap-pickups[k]
            #                 break
            #
            #



        # print(deliveries,pickups)

    answer = disTance
    return answer

print(solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))
