# Function to add an edge
def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# Function to display the adjacency list
def display(graph):
    for node in graph:
        print(node, "->", graph[node])

# Main program
graph = {
    'A': [],
    'B': [],
    'C': [],
    'D': []
}

addEdge(graph, 'A', 'B')
addEdge(graph, 'A', 'C')
addEdge(graph, 'B', 'D')
addEdge(graph, 'C', 'D')

display(graph)