class Solution:
    
    def visit(self, adj, visited, ans, n):
        if visited[n]:
            ans.append(n)
            visited[n]=0
            for i in adj[n]:
                self.visit(adj, visited, ans, i)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited={}
        for i in range(V):
            visited[i]=1
        ans=[]
        self.visit(adj,visited,ans,0)
        return ans