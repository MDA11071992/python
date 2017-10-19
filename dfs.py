# 1. Матрица связности.
g = [[0, 1, 0],  # матрица связности
     [1, 1, 0],
     [0, 0, 1]]

ex = set()  # множество посещенных вершин


def dfs(node):  # start - начальная вершина
    ex.add(node)
    for i in range(len(g)):
        if g[node][i] == 1 and i not in ex:
            print(i)
            dfs(i)


# 2. Список смежности.
list_of_adjacency = [[1, 3], [0], [3], [2, 0], []]
visited = [False for i in range(len(list_of_adjacency))]


def dfs(v):
    visited[v] = True
    for vertex in list_of_adjacency[v]:
        if not visited[vertex]:
            dfs(vertex)


for c in range(len(list_of_adjacency)):
    if not visited[c]:
        dfs(c)
