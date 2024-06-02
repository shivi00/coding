class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=n-2
        ans=[[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                val=-1
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        val=max(val,grid[k][l])
                ans[i][j]=val
        return ans