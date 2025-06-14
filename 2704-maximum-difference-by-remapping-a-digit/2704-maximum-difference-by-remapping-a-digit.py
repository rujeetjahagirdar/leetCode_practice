class Solution:
    def minMaxDifference(self, num: int) -> int:
        digit_to_remap = "-1"
        str_to_num = str(num)
        max_num = ''
        min_num = ''
        i=0

        while(i<len(str_to_num)):
            if(str_to_num[i]!="9"):
                digit_to_remap = str_to_num[i]
                break
            i+=1
        max_num = str_to_num.replace(digit_to_remap, '9')

        print(max_num)
        # print(str_to_num)

        i=0
        while(i<len(str_to_num)):
            if(str_to_num[i]!="0"):
                digit_to_remap = str_to_num[i]
                break
            i+=1
        min_num = str_to_num.replace(digit_to_remap, '0')

        print(min_num)
        # print(str_to_num)

        return(int(max_num)-int(min_num))