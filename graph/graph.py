from collections import defaultdict


class Graph:
    def __init__(self):
        self._graph = defaultdict(list)

    def add_edge(self, u, v):
        self._graph[u].append(v)
        self._graph[v].append(u)
    
