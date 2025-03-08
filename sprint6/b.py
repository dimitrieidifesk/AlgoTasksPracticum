def build_matrix(n, input_list: list):
    default_matrix = [['0' for j in range(n)] for i in range(n)]
    for i, j in input_list:
        default_matrix[i - 1][j - 1] = '1'

    return default_matrix

dlist = []
n, m = map(int, input().split())
for _ in range(m):
    dlist.append(map(int, input().split()))

r = build_matrix(n, dlist)
for s in r:
    print(' '.join(s))
