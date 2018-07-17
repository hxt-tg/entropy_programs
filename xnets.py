import networkx as nx

import numpy as np

class CircularNet(nx.Graph):
    """
    Create circular net with nodes from 0 to $n-1$.
    """
    def __init__(self, n):
        nx.Graph.__init__(self)
        if n <= 0:
            raise nx.NetworkXError('n should be greater than 0.')
        self.add_nodes_from(range(n))
        for i in range(n):
            self.add_edge(i, (i+1)%n)
        
class StarLikeNet(nx.Graph):
    """
    Create star like net with nodes 0 to $n-1$.
    """
    def __init__(self, n):
        nx.Graph.__init__(self)
        if n <= 1:
            raise nx.NetworkXError('n should be greater than 1.')
        self.add_nodes_from(range(n))
        for i in range(1, n):
            self.add_edge(0, i)
        i = np.random.randint(1, n-2)
        self.add_edge(i, i+1)
        
        
class RandomNMNet(nx.Graph):
    """
    Create random net with $n$ nodes and $m$ links (with no empty nodes).
    
    Nodes id from 0 to $n-1$.
    
    Special Exception:
        $m$ should be larger than $\left\lceil \frac n2 \right\rceil$.
    """
    def __init__(self, n, m):
        nx.Graph.__init__(self)
        if n <= 0:
            raise nx.NetworkXError('n should be larger than 0.')
        if m < np.ceil(n/2):
            raise nx.NetworkXError('m should be larger than ceil(n/2).')
        self.add_nodes_from(range(n))
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                self.add_edge(i, j)
                edges.append((i, j))
        while self.number_of_edges() > m:
            edge = edges[np.random.randint(0, len(edges))]
            if self.degree[edge[0]] < 2 or self.degree[edge[1]] < 2: continue
            edges.remove(edge)
            self.remove_edge(*edge)
        