class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # gcd(a, b) = gcd(b, a % b)
        #so unless second term becomes zero, we keep doing it and ans will be first term

        def gcd(a, b):
            if(b==0):
                return a
            return gcd(b, a%b)
        
        mn = min(nums)
        mx = max(nums)
        # print(mn, mx, gcd(mn, mx))
        return gcd(mn, mx)