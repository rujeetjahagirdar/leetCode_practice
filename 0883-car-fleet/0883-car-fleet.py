class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_reach = []
        cars = []

        for i in range(len(position)):
            time_remaining = (target - position[i])/speed[i]
            cars.append((position[i], speed[i], time_remaining))
        
        
        cars.sort(key=lambda x: x[0],reverse=True)
        print(cars)

        ans=0
        prev = float("-inf")
        for i in cars:
            if(i[2]>prev):
                ans+=1
                prev = i[2]
        
        return(ans)