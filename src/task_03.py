import networkx as nx

from algo import dijkstra
from task_01 import define_graph

weights = {
    ("a", "c"): 1,
    ("a", "b"): 4,
    ("a", "h"): 2,
    ("b", "c"): 6,
    ("c", "e"): 9,
    ("e", "h"): 10,
    ("e", "f"): 6,
    ("f", "g"): 8,
    ("d", "f"): 2,
    ("d", "g"): 1,
    ("h", "g"): 2,
}

nx.set_edge_attributes(define_graph, weights, "weight")


if __name__ == "__main__":
    print(dijkstra(define_graph, "h"))
