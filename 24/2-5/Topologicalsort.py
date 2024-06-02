#BFS
from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

        visited = {}
        for i in range(V):
            visited[i]=0
            
        for i in range(V):
            for j in adj[i]:
                visited[j]+=1
                    

            
        h = deque()
        for i in visited:
            if visited[i]==0:
                h.append(i)
        ans=[]
        while len(h):
            n = h.popleft()
            ans.append(n)
            for i in adj[n]:
                visited[i]-=1
                if visited[i]==0:
                    h.append(i)
        
        return ans
#DFS
from collections import deque
class Solution:
    
    def visit(self, adj, n, ans, visited):
        if adj[n]==[] and visited[n]:
            visited[n]=0
            ans.append(n)
        elif visited[n]:
            for i in adj[n]:
                self.visit(adj, i, ans, visited)
            visited[n]=0
            ans.append(n)
        
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):

        visited = {}
        for i in range(V):
            visited[i]=1
            
        ans=[]
        for i in range(V):
            self.visit(adj, i, ans, visited)
                
        
        return ans[::-1]
