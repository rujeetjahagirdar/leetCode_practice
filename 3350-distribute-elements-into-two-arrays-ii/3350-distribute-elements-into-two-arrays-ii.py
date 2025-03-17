class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        arr1_sorted = [nums[0]]
        arr2_sorted = [nums[1]]

        for i in range(2, len(nums)):
            count1 = (len(arr1_sorted)-bisect.bisect_right(arr1_sorted, nums[i]))
            count2 = (len(arr2_sorted)-bisect.bisect_right(arr2_sorted, nums[i]))

            if(count1>count2):
                arr1.append(nums[i])
                bisect.insort(arr1_sorted, nums[i])
            elif(count1<count2):
                arr2.append(nums[i])
                bisect.insort(arr2_sorted, nums[i])
            else:
                if(len(arr1)<len(arr2)):
                    arr1.append(nums[i])
                    bisect.insort(arr1_sorted, nums[i])
                elif(len(arr1)>len(arr2)):
                    arr2.append(nums[i])
                    bisect.insort(arr2_sorted, nums[i])
                else:
                    arr1.append(nums[i])
                    bisect.insort(arr1_sorted, nums[i])
        
        print(arr1+arr2)
        return arr1+arr2