from graph_interfaces import IEdge, IGraph, IVertex
from typing import List, Optional
from itertools import chain

# Implementation definitions
# You should implement the bodies of the methods required by the interface protocols.

class Graph(IGraph):    
    def __init__(self):
        self._vertices: List[IVertex] = []
        
    def get_vertices(self) -> List[IVertex]:
        return self._vertices
    
    def get_edges(self) -> List[IEdge]:
        return list(chain.from_iterable(x.get_edges() for x in self._vertices))
    
    def add_vertex(self, vertex: IVertex) -> None: 
        self._vertices.append(vertex)
        
    def remove_vertex(self, vertex_name: str) -> None:
        try:
            self._vertices.remove(vertex_name)
        except ValueError as err:
            raise IndexError(f'{vertex_name} is not a valid vertex') from err
        
    def add_edge(self, edge: IEdge) -> None:
        destination = edge.get_destination()
        vertex_i = self._vertices.index(destination)
        vertex = self._vertices[vertex_i]
        
        vertex.add_edge(edge)
        
    def remove_edge(self, edge_name: str) -> None:
        for vertex in self._vertices:
            # check ever edge in the current vertex if the edge name matches the edge to remove
            edge_match = list(filter(lambda x: x.get_name() == edge_name, vertex.get_edges())) != []
            
            if edge_match:
                vertex.remove_edge(edge_name)
                break
            

class Vertex(IVertex):
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name or ""
        self._edges: List[IEdge] = []
        self.visited = False
        
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
    def add_edge(self, edge: IEdge) -> None:
        self._edges.append(edge)
    
    def remove_edge(self, edge_name: str) -> None:
        try:
            self._edges.remove(edge_name)
        except ValueError as err:
            raise IndexError(f'{edge_name} is not a valid edge') from err
        
    def get_edges(self) -> List[IEdge]:
        return self._edges
    
    def set_visited(self, visited: bool) -> None:
        self.visited = visited
        
    def is_visited(self) -> bool:
        return self.visited
    
    def __str__(self):
        return f"<Vertex name={self.name}>"
    def __repr__(self):
        return f"<Vertex name={self.name}>"

class Edge(IEdge):
    def __init__(self, name: Optional[str] = None, weight: Optional[float] = None, destination: Optional[IVertex] = None):
        self.name = name or ""
        self.weight = weight or 0.0
        self.destination = destination
        
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
    def get_destination(self) -> IVertex:
        return self.destination
    
    def get_weight(self) -> float:
        return self.weight
    
    def set_weight(self, weight: float) -> None:
        self.weight = weight
        
    def __str__(self):
        return f"<Edge name={self.name} weight={self.weight} destination={repr(self.destination)}>"
    def __repr__(self):
        return f"<Edge name={self.name} weight={self.weight} destination={repr(self.destination)}>"
        