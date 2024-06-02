#BFS
from collections import deque
class Solution:
    
    

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        visited =[0]*n
        
        def bfs(n):
            if visited[n]:
                return True
            q=deque([n])

            visited[n]=-1
            while q:
                no = q.popleft()
                for ni in graph[no]:
                    if visited[ni]==visited[no]:
                        return False
                    elif not visited[ni]:
                        q.append(ni)
                        visited[ni]=-1*visited[no]
            return True
        
        for i in range(n):
            if not bfs(i):
                    return False
                
        return True
    

#DFS
from collections import deque
class Solution:
    
    def dfs(self,n,c,visited,graph):
        visited[n]=c
        for i in graph[n]:
            if visited[n]==visited[i]:
                return False
            elif visited[i]==0:
                if not self.dfs(i,c*-1,visited,graph):
                    return False
        return True
    
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        visited =[0 for i in range(n)]
        
        
    
        for i in range(n):
            if visited[i]==0 and not self.dfs(i,1,visited,graph):
                return False
                
        return True

# It is most effective solution cause with this less statements get executed