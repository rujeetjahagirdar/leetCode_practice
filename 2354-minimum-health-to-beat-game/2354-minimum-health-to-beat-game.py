class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        totalDamage = sum(damage)+1

        maxDamage = max(damage)

        if(maxDamage>=armor):
            totalDamage-=armor
        else:
            totalDamage-=maxDamage
        
        return totalDamage