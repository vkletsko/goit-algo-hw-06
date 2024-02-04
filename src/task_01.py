import networkx as nx
import matplotlib.pyplot as plt


define_graph = nx.DiGraph(
    [
        ("a", "c"),
        ("a", "b"),
        ("a", "h"),
        ("b", "c"),
        ("c", "e"),
        ("e", "h"),
        ("e", "f"),
        ("f", "g"),
        ("d", "f"),
        ("d", "g"),
        ("h", "g"),
    ]
)

for layer, nodes in enumerate(nx.topological_generations(define_graph)):
    for node in nodes:
        define_graph.nodes[node]["layer"] = layer

# Graph Visual options
edge_line_style = "dashed"
options = {
    "with_labels": True,
    "font_size": 10,
    "font_weight": "bold",
    "node_size": 700,
    "font_color": "white",
    "node_color": "blue",
    "width": 1.5,
    "style": edge_line_style,
}

if __name__ == "__main__":
    # Graph Info
    nodes_count = define_graph.number_of_nodes()
    edges_count = define_graph.number_of_edges()
    density = nx.density(define_graph)
    print(
        "Graph Info:",
        f"Nodes count: {nodes_count}",
        f"Edge count:{edges_count}",
        f"Density: {density:.5f}",
        sep="\n",
    )

    # Graph Visualization
    pos = nx.multipartite_layout(define_graph, subset_key="layer")
    fig, ax = plt.subplots()
    nx.draw_networkx(define_graph, pos=pos, ax=ax, **options)
    ax.set_title("Topograph")
    fig.tight_layout()
    plt.show()
