class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def enc(x):
            return (int(max(str(x))*len(str(x))))
        ans = 0
        for i in nums:
            ans +=enc(i)
        print(ans)
        return ans