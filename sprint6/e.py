from queue import Queue

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

colors = ['white'] * len(graph)

def bfs(s):
    path = []
    queue = Queue()
    queue.put(s)
    while not queue.empty():
        f = queue.get()
        path.append(f + 1)
        colors[f] = 'gray'
        for h in graph[f]:
            if colors[h] == 'white':
                queue.put(h)
                colors[h] = 'gray'
        colors[f] = 'black'
    return path

connectivity_components_paths = []

for i, vertexes in enumerate(graph):
    if colors[i] == 'white':
        path = bfs(i)
        path = sorted(path)
        if path not in connectivity_components_paths:
            connectivity_components_paths.append(path)

print(len(connectivity_components_paths))
for component in connectivity_components_paths:
    print(' '.join(map(str, sorted(component))))

