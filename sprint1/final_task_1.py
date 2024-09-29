# https://contest.yandex.ru/contest/22450/run-report/118701225/
from typing import List


def get_distance_matrix(arr: List[int]):
    last_empty_index = None
    new_arr = arr
    for i, plot in enumerate(arr):
        if plot == 0:
            if last_empty_index is None:
                # 4 5 0 -> 2 1 0
                for j in range(i + 1):
                    if new_arr[j] != 0:
                        new_arr[j] = i - j

                # 2 1 0 5 6 7 -> 2 1 0 1 2 3
                for j in range(i + 1, len(arr)):
                    if new_arr[j] != 0:
                        new_arr[j] = abs(i - j)
                    else:
                        break
            else:
                # 2 1 0 3 9 0 -> 2 1 0 1 1 0
                for j in range(last_empty_index + 1, i + 1):
                    if new_arr[j] != 0:
                        if abs(i - j) < new_arr[j]:
                            new_arr[j] = abs(i - j)
                # 2 1 0 1 1 0 6 7 19 -> 2 1 0 1 1 0 1 2 3
                for j in range(i + 1, len(arr)):
                    if new_arr[j] != 0:
                        new_arr[j] = abs(i - j)
                    else:
                        break
            last_empty_index = i
    return ' '.join(map(str, new_arr))


n = int(input())
arr = list(map(int, input().strip().split()))

print(get_distance_matrix(arr))
