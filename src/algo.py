from collections import deque


def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


def dijkstra(graph, start):
    dst = {n: float("inf") for n in graph.nodes()}
    dst[start] = 0

    visited = {n: False for n in graph.nodes()}

    while False in visited.values():
        cur_node = min(
            [node for node in graph.nodes() if visited[node] is False],
            key=lambda node: dst[node],
        )
        visited[cur_node] = True

        for neighbour, weight in graph[cur_node].items():
            if dst[cur_node] + weight["weight"] < dst[neighbour]:
                dst[neighbour] = dst[cur_node] + weight["weight"]

    return dst
