#BFS
class Solution:
    def dfs(self, n, m, i, j, h):
        if (i,j) in h and  h[(i,j)]==1:
            h[(i,j)]=0
            if i-1>-1:
                self.dfs(n, m, i-1, j, h)
            if j-1>-1:
                self.dfs(n, m, i, j-1, h)
            if i+1<n:
                self.dfs(n, m, i+1, j, h)
            if j+1<m:
                self.dfs(n, m, i, j+1, h)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        h = {}
        n=len(grid)
        m=len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    h[(i,j)]=1

        print(h)
        ans=0
        for i in h:
            if h[i]==1:
                self.dfs(n, m, i[0], i[1], h)
                ans+=1
            
        return ans
                