class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        self.follows[userId].add(userId)

        for followeeId in self.follows[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time , tweetId = self.tweets[followeeId][index]
                heapq.heappush(minheap, [time, tweetId, followeeId, index])

        while minheap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)

            if index - 1 >= 0:
                time , tweetId = self.tweets[followeeId][index- 1]
                heapq.heappush(minheap,[time, tweetId, followeeId, index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.follows[followerId] and followerId != followeeId:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)