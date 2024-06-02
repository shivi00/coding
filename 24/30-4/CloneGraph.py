class Solution:
    def visit(self,node,visited):
        if node not in visited and node:
            ans=Node(node.val,[])
            visited[node]= ans
            for i in node.neighbors:
                if i not in visited:
                    ans.neighbors.append(self.visit(i,visited))
                else:
                    ans.neighbors.append(visited[i])
            return ans
            
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited={}
        return self.visit(node,visited)