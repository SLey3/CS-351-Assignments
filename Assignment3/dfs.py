# Depth-First Search Algorithm (DFS)
from graph_interfaces import IGraph, IVertex

def _rec_dfs(graph: IGraph, visited: dict[str, IVertex], start_vertex_name: str, start_vertex_i: int, counter: int = 1) -> None:
    visited[start_vertex_name].set_visited(True)
    
    print(f"{counter}.", "Current Vertex:", start_vertex_name, sep=" ", end="\n")
    
    for vertex in graph.get_vertices()[start_vertex_i:]:
        if not vertex.is_visited():
            name = vertex.get_name()
            index = _find_index(graph.get_vertices()[start_vertex_i:], name)
            _rec_dfs(graph, visited, name, index, counter + 1)
    
    
def _find_index(vertices: list[IVertex], name: str) -> int:
    found_vertex = next(filter(lambda x: x.get_name() == name, vertices), None)
    
    if found_vertex is None:
        raise ValueError(f'Requested vertex with name: "{name}" might not exist')
    return vertices.index(found_vertex)
    

def dfs(graph: IGraph, start_vertex: IVertex) -> None:
    """
    Perform a depth-first search (DFS) on a graph starting from a given vertex.
    Args:
        graph (IGraph): The graph to traverse. It should provide methods to access its vertices.
        start_vertex (IVertex): The starting vertex for the DFS traversal. It should provide a method to get its name.
    Notes:
        - The function initializes a visited dictionary to set visited vertices.
        - It retrieves the name of the starting vertex and its index in the graph's vertex list.
        - The actual DFS traversal is performed by a recursive helper function `_rec_dfs`.
    """
    visited = {x: y for x, y in map(lambda z: (z.get_name(), z,), graph.get_vertices())}
    name = start_vertex.get_name()
    index = _find_index(graph.get_vertices(), name)
    
    # call recursive function
    _rec_dfs(graph, visited, name, index)
    