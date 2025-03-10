def build_adjacency_list(list_m):
    for u, v in list_m:
        print(u, v)


list_m = list()

n, m = map(int, input().split())
for _ in range(m):
    list_m.append(map(int, input().split()))

build_adjacency_list(list_m)