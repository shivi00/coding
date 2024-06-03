class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        s=sum(nums)
        m=[]
        n=len(nums)
        for i in range(n):
            d=(nums[i]^k)-(nums[i])
            m.append(d)
        m.sort(reverse=True)
        for i in range(0,n-1,2):
            if m[i]+m[i+1]>0:
                s+=(m[i]+m[i+1])
        return s