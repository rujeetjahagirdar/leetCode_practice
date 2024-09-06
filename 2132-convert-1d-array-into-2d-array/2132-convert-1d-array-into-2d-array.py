class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        ans = []
        for i in range(0,len(original), n):
            ans.append(original[i:i+n])

        print(ans)
        return ans