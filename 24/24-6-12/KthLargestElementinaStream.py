import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.vals = nums
        n=len(nums)
        heapq.heapify(self.vals)
        while len(self.vals)>k:
            heapq.heappop(self.vals)
                
        
    def add(self, val: int) -> int:
        heapq.heappush(self.vals,val)
        if len(self.vals)>self.k:
            heapq.heappop(self.vals)

        return self.vals[0]