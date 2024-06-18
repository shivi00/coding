import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stones_nv=[]
        for i in stones:
            stones_nv.append(-1*i)
        heapq.heapify(stones_nv)
        while len(stones_nv)>1:
            p=heapq.heappop(stones_nv)
            q=heapq.heappop(stones_nv)
            r=abs(p-q)
            if r>0:
                heapq.heappush(stones_nv,-1*r)
            print(len(stones_nv))
        s=sum(stones_nv)
        s*=-1
        return s