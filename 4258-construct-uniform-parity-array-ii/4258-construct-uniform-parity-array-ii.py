class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # smallest number will decide the parity of nums2,
            #if smallest number is even nums2 will have even parity
            #if smallest number is odd nums2 will have odd parity

        #if all are even, return True

        #if all are odd, return True
        
        #if smallest number is even, then we need to make nums2 all even
            # in this case, it is not possible to convert smallest odd number to even, since
            # to convert odd number to even, we need to substract another odd number from it, but since it is smallest odd number we dont have smaller odd number to substract.
        
        #if smallest number is odd, then we need to make nums2 all odd
            #in this case we keep all the odd values as it is and for even values we will substract this smallest odd value


        contains_odd = any(n%2==1 for n in nums1)
        contains_even = any(n%2==0 for n in nums1)

        if(contains_even and not contains_odd):
            return True
        
        if(contains_odd and not contains_even):
            return True
        
        if(min(nums1)%2==1):
            return True
        
        return False