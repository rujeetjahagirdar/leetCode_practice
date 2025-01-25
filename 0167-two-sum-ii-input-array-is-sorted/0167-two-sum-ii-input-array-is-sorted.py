class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # def bsearch(n, l, r):
        #     while(l<=r):
        #         mid = l+((r-l)//2)
        #         if(numbers[mid]==n):
        #             return mid
        #         elif(numbers[mid]<n):
        #             l=mid+1
        #         else:
        #             r=mid-1
        #     return None
            

        # for i in range(len(numbers)):
        #     compliment = target - numbers[i]
        #     compli_index = bsearch(compliment, i+1, len(numbers)-1)
            
        #     if(compli_index):
        #         return [i+1, compli_index+1]


        l=0
        r = len(numbers)-1

        while(l<=r):
            s = numbers[l]+numbers[r]

            if(s==target):
                return [l+1, r+1]
            elif(s<target):
                l+=1
            else:
                r-=1
        