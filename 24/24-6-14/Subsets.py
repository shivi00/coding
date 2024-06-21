class Solution(object):
    def subsets(self, nums):
        n=len(nums)
        res=[]
        s=[]
        def crtesbsts(i):
            if i==n and s not in res:
                res.append(s[:])
                return
            s.append(nums[i])
            crtesbsts(i+1)
            
            s.pop()
            crtesbsts(i+1)
            
        crtesbsts(0)
        return res