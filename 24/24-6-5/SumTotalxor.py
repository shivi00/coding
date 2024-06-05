class Solution:
    def subsetXORSum(self, nums: List[int]) -> int: 
        ans=[]
        n=len(nums)
        
        def create(i,a):
            if i==n:
                c=0
                if len(a)>0:
                    c=a[0]
                    a=a[1:]
                    for j in a:
                        c=c^j
                return c
            v1=a
            v2=a+[nums[i]]
            return create(i+1,v1)+create(i+1,v2)
        return create(0,[])