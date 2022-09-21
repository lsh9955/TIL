def SelectionSort(A,s):
    if s <= len(A)-1:
        minNum = A[s]
        minIdx = s
        for k in range(s,len(A)):
            if A[k]<minNum:
                minNum = A[k]
                minIdx = k
        A[minIdx],A[s] = A[s],A[minIdx]
        SelectionSort(A,s+1)
A = [2,4,6,1,9,8,7,0]
SelectionSort(A,0)
print(A)