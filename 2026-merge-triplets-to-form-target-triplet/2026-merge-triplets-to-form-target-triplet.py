class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # we actually don't need to simulate the logic, 
        # if using the candidates triplets we can form the target triplet at x place, at y place and at z place, then we can return True

        candidates = []
        x, y, z = target

        for i in range(len(triplets)):
            a, b, c = triplets[i]
        
            if(a<=x and b<=y and c<=z):
                candidates.append(triplets[i])
        
        print(candidates)
        
        x_found = False
        y_found = False
        z_found = False

        for i in range(len(candidates)):
            a, b, c = candidates[i]

            if(a==x):
                x_found = True
            if(b==y):
                y_found = True
            if(c==z):
                z_found = True
        
        if(x_found and y_found and z_found):
            return True
        return False