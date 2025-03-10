from queue import Queue

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

distances = [-1] * n


def bfs(s):
    queue = Queue()
    distances[s] = 0
    queue.put(s)
    while not queue.empty():
        f = queue.get()
        for h in graph[f]:
            if distances[h] == -1:
                queue.put(h)
                distances[h] = distances[f] + 1
    return distances


connectivity_components_paths = []

s = int(input())
bfs(s - 1)
print(max(distances))
