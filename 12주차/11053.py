N = int(input())
A = list(map(int,input().split()))
maxcount = 0
for a in range(N-1):
    thiscount = 1
    nownum = A[a]
    nowidx = -1
    afterlist = A[a+1:]
    for b in range(len(afterlist)):
        afterlist[b] = [b,afterlist[b]]
    afterlist.sort(key=lambda x:x[1])
    for b in range(len(afterlist)):
        if afterlist[b][1]>nownum and afterlist[b][0]>nowidx:
            nownum=afterlist[b][1]
            nowidx = afterlist[b][0]
            thiscount+=1
    if maxcount<thiscount:
        maxcount=thiscount
print(maxcount)


# 20 80 30 40 70 50 60

#  [30,2] [40,3]  [50,5][60,6][70,4] [80,1]