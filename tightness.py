import networkx as nx
from math import log

def network_density(net):
    return (2*net.number_of_edges())/(net.number_of_nodes()*(net.number_of_nodes()-1))

def entropy(net):
    Hg=0
    for i in range(net.number_of_nodes()):
        pi = net.degree[i]/(2*net.number_of_edges())
        Hg += pi * log(pi)
    Hg = -Hg
    return Hg

def community_tightness(net):
    return entropy(net)/log(net.number_of_nodes())*network_density(net)