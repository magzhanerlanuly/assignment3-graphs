from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, v):
        if v.id not in self.adjacency_list:
            self.adjacency_list[v.id] = []

    def add_edge(self, start_id, end_id):
        if start_id in self.adjacency_list:
            self.adjacency_list[start_id].append(end_id)

    def print_graph(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex}: {neighbors}")

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbor in self.adjacency_list.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start, visited=None, order=None):
        if visited is None:
            visited = set()
        if order is None:
            order = []
        visited.add(start)
        order.append(start)
        for neighbor in self.adjacency_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, order)
        return order