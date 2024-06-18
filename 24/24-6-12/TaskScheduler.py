import heapq
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        dic={}
        for i in tasks:
            if i not in dic:
                dic[i]=-1
            else:
                dic[i]-=1
        val=[]
        for i in dic:
            val.append(dic[i])
        heapq.heapify(val)
        c=0
        q=deque()
        while len(val)!=0 or len(q)!=0:
            if len(val)!=0:
                v=heapq.heappop(val)
                if v+1!=0:
                    q.append([v+1,c+n])
            while len(q)!=0:
                va,co=q[0]
                if co>c:
                    break
                else:
                    q.popleft()
                    heapq.heappush(val , va)
            c+=1
            
                    
        return c