class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # Shift result and add the last bit of n
            # print("result=", bin(result))
            n >>= 1  # Shift n to process the next bit
            # print(n)
        return result