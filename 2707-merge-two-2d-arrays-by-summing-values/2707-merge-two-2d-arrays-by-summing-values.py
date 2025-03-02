class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i=0
        j=0

        while(i<len(nums1) or j<len(nums2)):
            if(i<len(nums1)):
                if(j<len(nums2)):
                    id1 = nums1[i][0]
                    id2 = nums2[j][0]
                    if(id1==id2):
                        ans.append([id1, nums1[i][1]+nums2[j][1]])
                        i+=1
                        j+=1
                    elif(id1<id2):
                        ans.append([id1, nums1[i][1]])
                        i+=1
                    else:
                        ans.append([id2, nums2[j][1]])
                        j+=1
                else:
                    ans.append([nums1[i][0], nums1[i][1]])
                    i+=1
            else:
                if(j<len(nums2)):
                    ans.append([nums2[j][0], nums2[j][1]])
                    j+=1
        print(ans)
        return ans