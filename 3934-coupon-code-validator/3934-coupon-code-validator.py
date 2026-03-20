class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        ans=[]
        sorting_map = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        for i in range(len(code)):
            if(re.search(r"^[a-zA-Z0-9_]+$", code[i])):
                if(businessLine[i] in ("electronics", "grocery", "pharmacy", "restaurant")):
                    if(isActive[i]):
                        ans.append([code[i], businessLine[i]])
        
        # print(ans)
        ans.sort(key= lambda x: (sorting_map[x[1]], x[0]))

        return [i[0] for i in ans]