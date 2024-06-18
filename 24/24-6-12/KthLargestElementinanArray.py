import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        vals=[]
        for i in range(k):
            vals.append(nums[i])
        heapq.heapify(vals)
        n=len(nums)
        rest=[]
        for i in range(k,n):
            rest.append(nums[i])
        
        for i in rest:
            if i>vals[0]:
                heapq.heappop(vals)
                heapq.heappush(vals,i)
        return vals[0]