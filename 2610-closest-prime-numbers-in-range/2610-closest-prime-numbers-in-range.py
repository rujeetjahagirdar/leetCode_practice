class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n <= 1: return False
            if n <= 3: return True
            if n % 2 == 0 or n % 3 == 0: return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0: return False
                i += 6
            return True
        primes = [num for num in range(left, right + 1) if is_prime(num)]
        if len(primes) < 2: return [-1, -1]
        min_diff = float('inf')
        closest_pair = [-1, -1]
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                closest_pair = [primes[i], primes[i + 1]]
        return closest_pair
#Runtime Complexity: O(n sqrt(m)) where n is the range (right - left + 1) and m is the number being checked for primality
#Space Complexity: O(k) where k is the number of prime numbers in the given range