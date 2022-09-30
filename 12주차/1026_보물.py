N = int(input())
alist = list(map(int,input().split()))
blist = list(map(int,input().split()))
alist.sort(key=lambda x:-x)
blist.sort()
count = 0
for a in range(N):
    count+=alist[a]*blist[a]
print(count)