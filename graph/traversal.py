from graph import Graph

from collections import defaultdict


def bfs(graph, start):
    if start not in graph._graph:
        raise KeyError(f"Node {start} is not in the Graph {graph}")

    q = [] # for simlpicity reasons using list as queue
    visited = defaultdict(bool)
    q.append(start)

    while q:
        popped = q.pop(0)
        if popped not in visited:
            visited[popped] = True
            print(f"Visited node {popped}")

            for neighbor in graph._graph[popped]:
                if neighbor not in visited:
                    q.append(neighbor)


def dfs(graph, start):
    def _dfs(visited, node):
        visited[node] = True
        print(f"Visited node {node}")
        for neighbor in graph._graph[node]:
            if neighbor not in visited:
                _dfs(visited, neighbor)

    if start not in graph._graph:
        raise KeyError(f"Node {start} is not in the Graph {graph}")

    visited = defaultdict(bool)
    _dfs(visited, start)


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
 
    bfs(g, 'A')
    print()
    dfs(g, 'A')

