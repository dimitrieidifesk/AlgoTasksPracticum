from typing import List, Tuple


# https://contest.yandex.ru/contest/26365/problems/B/

def zipper(a: List[int], b: List[int]) -> List[int]:
    arr = list()
    for i, num in enumerate(a):
        arr.append(num)
        arr.append(b[i])
    return arr


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
