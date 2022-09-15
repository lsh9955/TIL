heap = []
def heap_push(item):
    heap.append(item)
    child = len(heap) - 1
    parent = child//2
    #부모가 본인보다 큰 경우, 자리를 바꿈(최소힙)
    #부모가 본인보다 작은 경우, 자리를 바꿈(최대힙)
    while parent and heap[parent] > heap[child]:
        heap[parent],heap[child] = heap[child], heap[parent]
        child = parent
        parent = child //2
    
def heap_pop():
    #pop은 없을 때 뽑히면 안됨
    if len(heap) == 1:
        return
    result = heap[1]
    item = heap.pop()
    heap[1] = item
    
    parent = 1 #루트부터 시작하므로
    child = parent*2 #일단 왼쪽이 작다고 가정함
    
    if child + 1 <= len(heap)-1:
        if heap[child] > heap[child+1]:
            child +=1
    
    
    return result