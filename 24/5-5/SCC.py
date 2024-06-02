#User function Template for python3

class Solution:
    def dfs(self,n,visited,adj,stack):
        visited[n]=0
        for i in adj[n]:
            if visited[i]!=0:
                self.dfs(i,visited,adj,stack)
        stack.append(n)
    
    def dfsT(self,n,visited,adjT):
        visited[n]=0
        for i in adjT[n]:
            if visited[i]!=0:
                self.dfsT(i,visited,adjT)
        return True
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        visited=[1 for _ in range(V)]
        stack=[]
        
        for i in range(V):
            if visited[i]!=0:
                self.dfs(i,visited,adj,stack)

        adjT=[[] for _ in range(V)]
        for i in range(V):
            visited[i]=1
            for j in adj[i]:
                adjT[j].append(i)
        
        scc=0
        while len(stack):
            no=stack.pop()
            if visited[no]!=0 and self.dfsT(no,visited,adjT):
                scc+=1
        return scc