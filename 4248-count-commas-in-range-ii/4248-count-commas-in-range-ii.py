class Solution:
    def countCommas(self, n: int) -> int:
        l = len(str(n)) #length of n

        ans=0

        if(l<=3):
            return 0
        
        for i in range(4, l):
            commas_per_number = (i-1)//3
            count_of_nums = 9 * pow(10, i-1)
            ans+= commas_per_number * count_of_nums
        

        commas_per_number = (l-1)//3
        count_of_nums = (n - pow(10, l-1)) + 1
        ans+= commas_per_number * count_of_nums

        return(ans)