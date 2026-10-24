class Solution:
    def minOperations(self, s: str) -> int:
        
        #already sorted return 0
        #if length is 2 and not already sorted, return -1, impossible case
        #if min char at 0th index or max char at n-1 th index, then return 1
        #if max char at 0th index or min char at n-1 th index, then three operations
            #max at 0th: sort s[0..n-2], it will move max char at n-2 nd index, then sort s[n-2..n-1], it will move max char to end, then sort s[0..n-2], it will give final sorted string, so total opeartions 3
            #min at n-1 th index: similar logic to above
        #if min or max char in middle of string: then sort s[0..n-2] for max char in middle or sort s[1..n-1] for min char in the middle, then sort either last two chars or first two char accordingly.

        sortedFlg=False
        mx, mn = max(s), min(s)
        n = len(s)

        if(n==1):
            return 0

        for i in range(n-1):
            if(s[i]<=s[i+1]):
                sortedFlg = True
            else:
                sortedFlg = False
                break
        
        if(sortedFlg==True):
            return 0
        
        if(n==2) and sortedFlg==False:
            return -1
        
        if(s[0]==mn or s[-1]==mx):
            return 1
        
        # if(s[0]==max(s) or s[-1]==min(s)):
        #     return 3
        
        for i in range(1, n-1):
            if(s[i]==mx or s[i]==mn):
                return 2
        
        if(s[0]==mx or s[-1]==mn):
            return 3