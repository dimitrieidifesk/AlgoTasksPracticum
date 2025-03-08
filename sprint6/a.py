def build_adjacency_list(n, list_m):
    res = [[] for _ in range(n)]
    for u, v in list_m:
        res[u - 1].append(str(v))
    return res


list_m = list()

n, m = map(int, input().split())
for _ in range(m):
    list_m.append(map(int, input().split()))

r = build_adjacency_list(n, list_m)
for i, s in enumerate(r):
    print(len(s), ' '.join(s))
