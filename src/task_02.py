from task_01 import define_graph
from algo import dfs, bfs

if __name__ == "__main__":
    print("DFS algorithm")
    dfs(define_graph, "e")
    print("\n")
    print("BFS algorithm")
    bfs(define_graph, "e")
    print("\n")
