import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        vals=[]
        for c,v in enumerate(points):
            x,y=v
            vals.append([sqrt(x**2+y**2),c])
        heapq.heapify(vals)
        ans=[]
        while k!=0:
            d,c= heapq.heappop(vals)
            ans.append(points[c])
            k-=1
        return ans