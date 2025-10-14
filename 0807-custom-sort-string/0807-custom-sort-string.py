class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        #count freq of each char in s
        #form a string according to order

        #TC: O(length of s)
        #SC: O(length of s)

        c = Counter(s)
        #{'a':1, 'b':1, 'c':1, 'd':1}
        ans=''

        for i in order:
            if(i in c):
                ans+=i*c[i]
                c[i]=0
        
        for i in c:
            if(c[i]!=0):
                ans+=i*c[i]
                c[i]=0
        
        return ans
