class Twitter:

    def __init__(self):
        self.time=  0
        self.following = defaultdict(set)
        self.feeds = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feeds[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        max_heap = []

        self.following[userId].add(userId)

        for usr in self.following[userId]:
            if(len(self.feeds[usr])>0):
                timestamp, tId = self.feeds[usr][-1]
                heapq.heappush(max_heap, (-timestamp, tId, usr, len(self.feeds[usr])-1))
        
        while(len(ans)<10 and max_heap):
            ts, tId, usr, idx = heapq.heappop(max_heap)
            ans.append(tId)

            if(idx-1>=0):
                timestamp, tId = self.feeds[usr][idx-1]
                heapq.heappush(max_heap, (-timestamp, tId, usr, idx-1))
        
        print(ans)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followeeId in self.following[followerId]):
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)