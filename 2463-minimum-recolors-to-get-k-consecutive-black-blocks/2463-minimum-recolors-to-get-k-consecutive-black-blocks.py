class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        changes = blocks[:k].count('W')
        print(changes)
        t=changes
        for i in range(1,len(blocks)-k+1):
            # print(blocks[i:i+k])
            # if(blocks[i-1]=='W'):
            #     t-=1
            # if(blocks[i+k]=='W'):
            #     t+=1
            t = blocks[i:i+k].count('W')
            changes=min(changes,t)
        
        print(changes)
        return changes