import sys

def bfs(n, graph, start):
    visited, queue = set(), [start]
    distances = dict()
    for i in range(n):
        distances[i] = -1
    distances[start] = 0
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
            for neighbour in graph[vertex]:
                if distances[neighbour] == -1 or distances[neighbour] > distances[vertex] + 6:
                    distances[neighbour] = distances[vertex] + 6
    return distances

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num_nodes, num_edges = [int(x) for x in input().split()]
        graph = dict()
        for i in range(num_nodes):
            graph[i] = set()
        for _ in range(num_edges):
            e1, e2 = [int(x) - 1 for x in input().split()]
            graph[e1].add(e2)
            graph[e2].add(e1)
        start = int(input()) - 1
        print(" ".join([str(x) for i, x in bfs(num_nodes, graph, start).items() if i != start]))
