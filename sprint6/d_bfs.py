from queue import Queue

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

color = ['white'] * len(graph)  # Инициализация цветов

for neighbors in graph:
    neighbors.sort()

vertexes = []

def bfs(s):
    # Создадим очередь вершин и положим туда стартовую вершину.
    planned = Queue()
    planned.put(s)
    color[s] = 'gray'
    while not planned.empty():
        u = planned.get()  # Возьмём вершину из очереди.
        vertexes.append(str(u + 1))
        for v in graph[u]:
            if color[v] == 'white':
                color[v] = 'gray'
                planned.put(v)  # Запланируем посещение вершины.
        color[u] = 'black'  # Теперь вершина считается обработанной.


start = int(input()) - 1
bfs(start)
print(' '.join(vertexes))
