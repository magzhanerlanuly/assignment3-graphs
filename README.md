# Assignment 4: Graph Traversal and Representation System

## Project Overview
This project implements a graph representation system using an **Adjacency List**. It includes two primary traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to analyze their performance across different graph sizes.

## Class Descriptions
- **Vertex**: Represents a node in the graph with a unique identifier.
- **Edge**: Represents a connection between two vertices.
- **Graph**: Manages the adjacency list and implements traversal logic.
- **Experiment**: Handles automatic graph generation and performance measurement using nanoseconds.

## Algorithm Descriptions
### BFS (Breadth-First Search)
- **Logic**: Visits all neighbors at the current depth before moving to the next level using a queue.
- **Complexity**: O(V + E)
- **Use Case**: Finding the shortest path in unweighted graphs.

### DFS (Depth-First Search)
- **Logic**: Explores as far as possible along each branch before backtracking using recursion or a stack.
- **Complexity**: O(V + E)
- **Use Case**: Solving puzzles or detecting cycles in a graph.

## Experimental Results
The following measurements were taken on a MacBook Air:

| Size (Vertices) | BFS (ns) | DFS (ns) |
| :--- | :--- | :--- |
| 10 | 12125 | 3667 |
| 30 | 7125 | 2083 |
| 100 | 41750 | 87708 |

## Analysis and Observations
- **Graph Size Impact**: As the number of vertices increases, the execution time for both algorithms generally increases, following the O(V + E) complexity.
- **Speed**: In these experiments, DFS showed faster execution for smaller graphs, while performance varies as the graph structure becomes more complex.
- **DFS Limitations**: DFS can face recursion depth limits on very deep graphs and doesn't guarantee the shortest path.
- **BFS Preference**: BFS is preferred when the goal is to find the shortest path from the starting node.

## Screenshots
![Performance Results](docs/results.jpg)

## Reflection Section
Through implementing this project, I gained a hands-on understanding of graph representations and traversals. Transitioning from abstract concepts to coding an Adjacency List made it clear how structural choices directly impact performance. Learning how Breadth-First Search relies on a queue layout to explore level-by-level, while Depth-First Search utilizes recursive call stacks to plunge deep into paths, highlighted how fundamentally different these two approaches are despite solving similar traversal problems.

One of the main challenges faced during the implementation was managing performance benchmarking accurately. Since initial system actions and JVM/Python interpreter warm-ups can distort runtime metrics on smaller inputs, ensuring consistent constraints across graphs with 10, 30, and 100 vertices required running clean execution blocks. Additionally, visually tracking and validating traversal order paths to prevent infinite loops in cyclic components provided a great exercise in core algorithmic logic.