# ...existing code...
from graph_interfaces import IGraph, IVertex
from collections import deque

def bfs(graph: IGraph, start_vertex: IVertex) -> None:
    """
    Performs a Breadth-First Search (BFS) traversal on a graph starting from a given vertex.

    Args:
        graph (IGraph): The graph to traverse.
        start_vertex (IVertex): The starting vertex for the BFS traversal.

    Behavior:
        - Resets the visited status of all vertices in the graph.
        - Traverses the graph in BFS order starting from the `start_vertex`.
        - Marks each visited vertex to avoid revisiting.
        - Prints the traversal steps in the order vertices are visited.

    Note:
        This function does not return any value. It is intended for traversal and
        printing purposes only.
    """
    # Reset visited on all vertices
    for v in graph.get_vertices():
        v.set_visited(False)

    q: deque[IVertex] = deque()
    counter = 1

    # Initialize Start Vertex
    start_vertex.set_visited(True)
    q.append(start_vertex)

    while q:
        current = q.popleft()
        print(f"{counter}.", "Current Vertex:", current.get_name(), sep=" ")
        counter += 1

        for edge in current.get_edges():
            neighbor = edge.get_destination()
            if not neighbor.is_visited():
                neighbor.set_visited(True)
                q.append(neighbor)
                