from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge

from dfs import dfs
from bfs import bfs

from typing import Optional
import pandas as pd

def read_graph(file_path: str) -> IGraph:  
    """Read the graph from the file and return the graph object"""
    df = pd.read_csv(file_path)
    
    graph = Graph()
    vertices: dict[str, Vertex] = {}

    def ensure_vertex(name: str) -> Vertex:
        if name not in vertices:
            v = Vertex(name)
            vertices[name] = v
            graph.add_vertex(v)
        return vertices[name]

    for _, row in df.iterrows():
        src_name = str(row["source"]).strip()
        dst_name = str(row["destination"]).strip()
        highway = str(row.get("highway", "")).strip()
        dist = row.get("distance")

        if src_name == "" or dst_name == "":
            continue

        src_v = ensure_vertex(src_name)
        dst_v = ensure_vertex(dst_name)

        weight = float(dist) if dist is not None and str(dist).strip() != "" else None

        # use highway as edge name, store edge on the source vertex
        edge = Edge(name=highway or dst_name, weight=weight, destination=dst_v)
        src_v.add_edge(edge)
    
    return graph

def print_dfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the DFS traversal of the graph starting from the start vertex"""
    print("Running DFS Algorithm...\n\n")
    
    dfs(graph, start_vertex)
    print("---------------------")

def print_bfs(graph: IGraph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex"""
    print("\n\n\nRunning BFS Algorithm...\n\n")
    
    bfs(graph, start_vertex)


def main() -> None:
    graph: IGraph = read_graph("data/graph.txt")
    start_vertex_name: str  = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()