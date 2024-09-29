# https://contest.yandex.ru/contest/22450/run-report/118702342/
from typing import List


def get_win_count(k: int, matrix: List[str]):
    unique_nums = {}
    for i in matrix:
        for j in i:
            if j != '.':
                if unique_nums.get(j):
                    unique_nums[j] += 1
                else:
                    unique_nums[j] = 1
    win_count = 0
    for t in list(unique_nums.keys()):
        if unique_nums[t] <= 2 * k:
            win_count += 1
    return win_count


k = int(input())
matrix = []
for _ in range(4):
    matrix.append(input().strip())

print(get_win_count(k, matrix))
