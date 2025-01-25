class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def bsearch(n, l, r):
            while(l<=r):
                mid = l+((r-l)//2)
                if(numbers[mid]==n):
                    return mid
                elif(numbers[mid]<n):
                    l=mid+1
                else:
                    r=mid-1
            return None
            

        for i in range(len(numbers)):
            compliment = target - numbers[i]
            compli_index = bsearch(compliment, i+1, len(numbers)-1)
            print(numbers[i])
            print(compli_index)
            # print(numbers[compli_index])
            if(compli_index):
                return [i+1, compli_index+1]