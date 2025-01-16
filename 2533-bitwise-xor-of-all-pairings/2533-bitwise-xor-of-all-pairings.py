class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        #(a1^b1)^(a1^b2)^(a1^b3)^(a1^b4)^......
        #(a1^a1^a1^a1^.....[n2 times])...^(b1^b1^b1^.....[n1 times])


        c1 = Counter(nums1)
        c2 = Counter(nums2)

        ans=0
        
        if(len(nums2)%2!=0):
            for i in c1:
                if(c1[i]%2!=0):
                    ans^=i
        
        if(len(nums1)%2!=0):
            for i in c2:
                if(c2[i]%2!=0):
                    ans^=i
        print(ans)
        return ans