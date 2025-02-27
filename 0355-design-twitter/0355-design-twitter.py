import heapq
from typing import List

class Twitter:
    def __init__(self):
        # Map user -> set of followees
        self.followees = {}
        
        # Map user -> list of (time, tweetId) for all tweets posted by user
        self.tweets = {}
        
        # Global timestamp to order tweets
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Composes a new tweet with ID tweetId by the user userId.
        Each call is guaranteed to have a unique tweetId.
        """
        if userId not in self.tweets:
            self.tweets[userId] = []
        # Add the tweet along with the current global timestamp
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed.
        The feed includes the user's own tweets and tweets from the users
        they follow. Tweets are ordered from most recent to least recent.
        """
        # Collect all users we need to look at: the user and everyone they follow
        users_to_check = set()
        users_to_check.add(userId)
        
        if userId in self.followees:
            for followeeId in self.followees[userId]:
                users_to_check.add(followeeId)
        
        # Max-heap (in Python we'll use a min-heap with negative timestamps)
        # We'll push the most recent tweet of each user. 
        # Then pop from heap and add the next older tweet from the same user.
        heap = []
        
        for u in users_to_check:
            if u in self.tweets and len(self.tweets[u]) > 0:
                # The most recent tweet is at the end of the list
                time, tId = self.tweets[u][-1]
                # We'll store (negative_time, tId, index_in_list, userId)
                # so that the largest time has the highest priority (i.e., smallest negative_time).
                heapq.heappush(heap, (-time, tId, len(self.tweets[u]) - 1, u))
        
        result = []
        
        # Extract up to 10 tweets
        while heap and len(result) < 10:
            neg_time, tId, idx, u = heapq.heappop(heap)
            result.append(tId)
            
            # If there is an older tweet for this user, push it onto the heap
            if idx - 1 >= 0:
                older_time, older_tId = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-older_time, older_tId, idx - 1, u))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId starts following the user with ID followeeId.
        """
        if followerId == followeeId:
            return  # Typically, do nothing if a user tries to follow themselves
        
        if followerId not in self.followees:
            self.followees[followerId] = set()
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        The user with ID followerId stops following the user with ID followeeId.
        """
        if followerId in self.followees:
            # Do not remove if followerId == followeeId to avoid unfollowing oneself
            # if we are treating self-follow as always on. (Adjust per requirement.)
            if followeeId in self.followees[followerId]:
                self.followees[followerId].remove(followeeId)

# Usage example:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# feed = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)
