def sift_up(heap, index):
    current = index

    while current > 1:
        parent = current // 2
        if heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
            current = parent
        else:
            break

    return current