n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

for neighbors in graph:
    neighbors.sort()

s = int(input()) - 1

visited = [False] * n
order = []
stack = [s]

while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = True
        order.append(v + 1)
        for neighbor in reversed(graph[v]):
            if not visited[neighbor]:
                stack.append(neighbor)

print(' '.join(map(str, order)))
