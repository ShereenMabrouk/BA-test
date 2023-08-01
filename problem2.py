'''
(2) A tool for finding and sketching loops in a graph (network) defined by edges in a CSV file 
(i.e., 2 columns, column A is the source node, column B is the target node, and a node is represented as an arbitrary string of characters).

'''
import csv
import networkx as nx
import matplotlib.pyplot as plt

def read_graph_from_csv(csv_file):
    graph = nx.DiGraph()
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            graph.add_edge(row['source'], row['target'])
    return graph

def find_loops(graph):
    loops = []
    for node in graph.nodes():
        for path in nx.all_simple_paths(graph, node, node):
            if len(path) > 1:
                loops.append(path)
    return loops

def sketch_graph(graph):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10)
    plt.show()

def main():
    csv_file = 'graph.csv'
    graph = read_graph_from_csv(csv_file)
    loops = find_loops(graph)

    if loops:
        print("Loops found in the graph:")
        for loop in loops:
            print(" -> ".join(loop))
    else:
        print("No loops found in the graph.")

    sketch_graph(graph)

if __name__ == "__main__":
    main()
