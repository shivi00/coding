import heapq
class MedianFinder(object):

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minheap)==len(self.maxheap):
            if (len(self.maxheap)!=0 and -1*num>=self.maxheap[0]):
                heapq.heappush(self.maxheap,-1*num)
                v=heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap,-1*v)
            else:
                heapq.heappush(self.minheap,num)
        else:
            if (len(self.maxheap)!=0 and -1*num>=self.maxheap[0]):
                heapq.heappush(self.maxheap,-1*num)
            else:
                heapq.heappush(self.minheap,num)
                v=heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap,-1*v)
            
                
        

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.minheap)+len(self.maxheap))%2==0:
            return ((self.maxheap[0]*-1+self.minheap[0])/2.00000)
        else:
            return self.minheap[0]