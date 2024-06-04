#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        rem=[0 for i in range(V)]
        dist=[0 if i==S else 100000000  for i in range(V)]
        for i in range(V):
            c=0
            for u,v,w in edges:
                if i==V-1 and dist[u]!=100000000 and dist[u]+w<dist[v]:
                    return [-1]
                if dist[u]+w>=dist[v]:
                    c+=1
                if dist[u]!=100000000  and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
                
            if c==len(edges):
                break
                    
        return dist

