class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime_numbers = [True]*(n+1)
        prime_numbers[0], prime_numbers[1] = False, False
        for i in range(2, int(math.sqrt(n))+1):
            if(prime_numbers[i]==True):
                for j in range(i*i, n+1, i):
                    prime_numbers[j]=False
        primes = []
        for i in range(len(prime_numbers)):
            if(prime_numbers[i]):
                primes.append(i)
        
        # print(primes)

        ans=[]
        for i in range(len(primes)):
            target = n-primes[i]
            if(target<primes[i]):
                break
            elif(prime_numbers[target]==True):
                ans.append([primes[i],target])
        print(ans)
        return ans