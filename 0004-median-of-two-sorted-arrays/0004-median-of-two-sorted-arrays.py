class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1.extend(nums2)
        # nums1.sort()
        # n=len(nums1)
        # if(n%2==0):
        #     return (nums1[(n//2)-1] + nums1[(n//2)])/2
        # else:
        #     return nums1[(n//2)]

        m = len(nums1)
        n = len(nums2)

        nums1.extend(['x']*n)

        i=m-1
        j=n-1
        k=m+n-1
        print("Extended nums1= ",nums1)
        while(j>=0):
            # print(i, j)
            # print(nums2[j])
            if(i>=0 and nums1[i]>=nums2[j]):
                nums1[k]=nums1[i]
                k-=1
                i-=1
                # if nums1[i]>=nums2[j]:
                #     j-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            # print(nums1)
        print(j)
        if((m+n)%2==0):
            return (nums1[((m+n)//2)-1] + nums1[((m+n)//2)])/2 
        else:
            return nums1[(m+n)//2]