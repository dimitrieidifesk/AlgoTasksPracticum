from queue import Queue

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

s, t = map(int, input().split())

colors = ['white'] * len(graph)

def relax(u, v):
    # Проверяем, не получился ли путь короче найденного ранее.
    if dist[v] > dist[u] + weight(u, v):
        dist[v] = dist[u] + weight(u, v)
        previous[v] = u


def get_min_dist_not_visited_vertex():
    # Находим ещё непосещённую вершину с минимальным расстоянием от s.
    current_minimum = math.inf
    current_minimum_vertex = -1

    for v in graph.vertices:
        if not visited[v] and dist[v] < current_minimum:
            current_minimum = dist[v]
            current_minimum_vertex = v

    return current_minimum_vertex


def dijkstra(graph, s):
    for v in graph.vertices:
        dist[v] = math.inf    # Задаём расстояние по умолчанию.
        previous[v] = -1      # Задаём предшественника для восстановления SPT.
        visited[v] = False    # Список статусов посещённости вершин.

    dist[s] = 0     # Расстояние от вершины до самой себя 0.

    while True:
        u = get_min_dist_not_visited_vertex()
        if u == -1 or dist[u] == math.inf:
            break

        visited[u] = True
        # из множества рёбер графа выбираем те, которые исходят из вершины u
        neighbours = graph.outgoing_edges(u)

        for v in neighbours:
            relax(u, v)