class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]

        if(a==b==c):
            return "equilateral"
        # elif(a==b or b==c or a==c):
        #     return "isosceles"
        elif((a+b > c) and (a+c > b) and (b+c > a)):
            if(a==b or b==c or a==c):
                return "isosceles"
            return "scalene"
        else:
            return "none"