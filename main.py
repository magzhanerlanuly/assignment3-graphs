from graph import Graph
from vertex import Vertex
from experiment import Experiment

def main():
    exp = Experiment()
    sizes = [10, 30, 100]
    
    print(f"{'Size':<10} | {'BFS (ns)':<15} | {'DFS (ns)':<15}")
    print("-" * 45)
    
    for size in sizes:
        g = exp.create_random_graph(size)
        bfs_t, dfs_t = exp.run_traversals(g, 0)
        print(f"{size:<10} | {bfs_t:<15} | {dfs_t:<15}")

if __name__ == "__main__":
    main()  
print("\n--- BONUS TASK: Dijkstra & Adjacency Matrix ---")
matrix_sample = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
bonus_graph = Graph()
bonus_graph.load_from_matrix(matrix_sample)
print("Graph loaded from Adjacency Matrix:")
bonus_graph.print_graph()

shortest_paths = bonus_graph.dijkstra(0)
print(f"Shortest paths from node 0 using Dijkstra: {shortest_paths}")