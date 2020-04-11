#Uses python3

import sys
import queue


# this function takes an an adjacent list representation of an undirected graph,
# a pair of vertices s and t, and returns the distance from s to t
# the function uses a queue (FIFO) to keep track of the vertices during breadth-first-search
def distance(adj, s, t):
    n = len(adj) # number of vertices in the graph
    root = s # choose s as the starting/ root vertex from which distance will be calculated
    dist = [-1 for _ in range(n)] # initialize distance from all points to s to be -1
    dist[root] = 0 # except for distance from the root to itself, which is 0
    # add the root vertex to the queue and start processing vertices one by one off the queue and layer by layer
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        v = q.get() # pop off one vertex from the queue and explore this vertex
        for adj_node in adj[v]:
            if adj_node != v: # ignore all loops
                if dist[adj_node] == -1: # ignore all nodes previously visited whose distance has been updated and not equal to -1
                    q.put(adj_node)
                    dist[adj_node] = dist[v] + 1 # update distance. if a node is adjacent and not yet visited, it must be located in the next layer

    return dist[t] # return distance between s and t


# this program reads the input, builds an adjacent list (adj) representation of an undirected graph from input,
# and prints the distance from a pair of vertices (s, t)
# if the two vertices are not reachable from one another, print -1
# EXAMPLE 1:
# input given in 1-based index (and how to interpret input):
# 4 4 (n = number of vertices = 4; m = number of edges = 4)
# 1 2 (an undirected edge between vertex 1 and 2)
# 4 1 (an undirected edge between vertex 4 and 1)
# 2 3 (an undirected edge between vertex 2 and 3)
# 3 1 (an undirected edge between vertex 3 and 1)
# 2 4 (measure distance between vertex 2 and 4)
# output: 2
# EXAMPLE 2:
# input:
# 5 8
# 4 1
# 4 1
# 1 1
# 3 5
# 1 4
# 5 2
# 4 2
# 4 2
# 4 3
# output: 3
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
