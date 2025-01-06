def sift_down(heap, index):
    n = len(heap) - 1
    current = index

    while True:
        left = 2 * current
        right = 2 * current + 1
        largest = current

        if left <= n and heap[left] > heap[largest]:
            largest = left

        if right <= n and heap[right] > heap[largest]:
            largest = right

        if largest == current:
            break

        heap[current], heap[largest] = heap[largest], heap[current]
        current = largest

    return current


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()