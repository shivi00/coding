#DFS
class Solution:
    
    def visit(self, adj, visited, n):
        if n in visited:
                return False
        if adj[n]==[]:
            return True
        visited.add(n)
        for i in adj[n]:
            if not self.visit(adj, visited, i):
                return False
        visited.remove(n)
        adj[n]=[]
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj =[[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[0]].append(i[1])
        for i in range(numCourses):
            if not self.visit(adj,set(),i):
                return False
            
        return True