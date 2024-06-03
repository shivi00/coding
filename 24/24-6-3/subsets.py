class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        
        def create(i,a):
            if i==n:
                if a not in ans:
                    ans.append(a)
                return
            v1=a
            v2=a+[nums[i]]
            create(i+1,v1)
            create(i+1,v2)
        create(0,[])
        return ans