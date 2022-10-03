import sys

input = sys.stdin.readline
K,L = list(map(int,input().split()))
suganglist = [input().strip() for _ in range(L)]
sugangdict = {}
for a in range(L):
    sugangdict[suganglist[a]]=a
sortsugang = sorted(sugangdict.items(), key=lambda x:x[1])
for b in range(K):
    print(sortsugang[b][0])
    if len(sortsugang)-1==b:
        break
