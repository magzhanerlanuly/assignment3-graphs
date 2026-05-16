import time
import random
from graph import Graph
from vertex import Vertex

class Experiment:
    def run_traversals(self, g, start_node):
        start_time = time.perf_counter_ns()
        g.bfs(start_node)
        bfs_time = time.perf_counter_ns() - start_time

        start_time = time.perf_counter_ns()
        g.dfs(start_node)
        dfs_time = time.perf_counter_ns() - start_time
        
        return bfs_time, dfs_time

    def create_random_graph(self, size):
        g = Graph()
        for i in range(size):
            g.add_vertex(Vertex(i))
        for i in range(size * 2):
            u = random.randint(0, size - 1)
            v = random.randint(0, size - 1)
            if u != v:
                g.add_edge(u, v)
        return g