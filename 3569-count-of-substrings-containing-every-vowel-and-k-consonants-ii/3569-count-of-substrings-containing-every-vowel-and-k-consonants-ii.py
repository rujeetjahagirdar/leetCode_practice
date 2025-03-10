class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atLeastK(word, k):
            vowels = 'aeiou'
            vowels_count = defaultdict(int)
            non_vowels = 0
            ans=0

            l=0
            
            for r in range(len(word)):
                if(word[r] in vowels):
                    vowels_count[word[r]]+=1
                else:
                    non_vowels+=1
                
                while(len(vowels_count)==len(vowels) and non_vowels>=k):
                    ans+=(len(word)-r)
                    if(word[l] in vowels):
                        vowels_count[word[l]]-=1
                        if(vowels_count[word[l]]==0):
                            vowels_count.pop(word[l])
                    else:
                        non_vowels -=1
                    
                    l+=1
                # if(len(vowels_count)==len(vowels) and non_vowels==k):
                #     ans+=1


            return ans
        
        ans1 = atLeastK(word, k)
        ans2 = atLeastK(word, k+1)
        print(ans1-ans2)
        return (ans1-ans2)