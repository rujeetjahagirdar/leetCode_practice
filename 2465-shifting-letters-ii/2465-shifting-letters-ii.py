class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # moves = [0]*len(s)

        # for start, end, direction in shifts:
        #     if(direction==1):
        #         for i in range(start, end+1):
        #             moves[i]+=1
        #     else:
        #         for i in range(start, end+1):
        #             moves[i]-=1
        
        # print(moves)

        # ans=''
        
        # for i in range(len(s)):
        #     c_ascii = ord(s[i])
        #     new_c = chr(((c_ascii - ord('a'))+moves[i])%26 + ord('a'))
        #     # print(new_c)
        #     ans+=new_c
        # print(ans)
        # return ans
        ######################

        moves = [0]*(len(s)+1)

        for start, end, direction in shifts:
            if(direction==1):
                moves[start]+=1
                moves[end+1]-=1
            else:
                moves[start]-=1
                moves[end+1]+=1
        
        print(moves) #[0, 1, 1, -2]

        for i in range(1, len(moves)):
            moves[i]+=moves[i-1]
        
        print(moves) #[0, 1, 2, 0]

        ans=[]

        for i in range(len(s)):
            c_ascii = ord(s[i])
            new_c = chr(((c_ascii - ord('a'))+moves[i])%26 + ord('a'))
            ans.append(new_c)
        print(ans)
        return ''.join(ans)