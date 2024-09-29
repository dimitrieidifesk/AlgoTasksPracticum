# https://contest.yandex.ru/contest/22779/problems/?nc=BCbIkt6e
from typing import List


def transpose(n: int, m: int, matrix: List[List[int]]):
    for i in range(m):
        new_row = []
        for j in range(n):
            new_row.append(matrix[j][i])
        print(' '.join(map(str, new_row)))


n = int(input())
m = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().strip().split())))

transpose(n, m, matrix)
