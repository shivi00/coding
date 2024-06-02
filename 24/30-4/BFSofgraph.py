from typing import List
from queue import Queue

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        ans=[]
        visited={}
        for i in range(V):
            visited[i]=1
        q = Queue()
        q.put(0)
        visited[0]=0
        while not q.empty():
            n=q.get()
            ans.append(n)
            for i in adj[n]:
                if visited[i]:
                    q.put(i)#visiting the nodes
                    visited[i]=0
        return ans
