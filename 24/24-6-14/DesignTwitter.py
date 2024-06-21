import heapq
class Twitter(object):

    def __init__(self):
        self.count =10000
        self.tweetmp = []
        heapq.heapify(self.tweetmp)
        self.followmp = defaultdict(set)
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        heapq.heappush(self.tweetmp,[self.count,tweetId,userId])
        self.count-=1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res=[]
        rem=[]
        self.followmp[userId].add(userId)
        while len(self.tweetmp)!=0 and len(res)<10:
            val=heapq.heappop(self.tweetmp)
            if val[-1] in self.followmp[userId]:
                res.append(val[1])
            rem.append(val)
        while len(rem)!=0:
            val = rem.pop()
            heapq.heappush(self.tweetmp,val)
        return res
            
            
        
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followmp[followerId].add(followeeId)
            
            
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followmp[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)