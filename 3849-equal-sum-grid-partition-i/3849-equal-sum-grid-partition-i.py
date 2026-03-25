class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        rowsum = defaultdict(int)
        totalrow = 0

        for rowidx in range(len(grid)):
            rowsum[rowidx] = sum(grid[rowidx])
            totalrow+=rowsum[rowidx]
        
        print(f"rowsum= {rowsum}, totalrow= {totalrow}")

        if(totalrow%2 !=0):
            return False
        
        colsum = defaultdict(int)
        totalcol = 0

        for colidx in range(len(grid[0])):
            for rowidx in range(len(grid)):
                colsum[colidx]+=grid[rowidx][colidx]
            totalcol+=colsum[colidx]
        
        print(f"colsum= {colsum}, totalcol= {totalcol}")

        if(totalcol%2 !=0):
            return False

        rowsumvals = list(rowsum.values())
        cumrowSum = 0
        target  = totalrow //2
        for i in range(len(rowsumvals)):
            cumrowSum+=rowsumvals[i]
            if(cumrowSum==target):
                return True
        

        colsumvals = list(colsum.values())
        cumcolSum=0
        target = totalcol//2
        for i in range(len(colsumvals)):
            cumcolSum +=colsumvals[i]
            if(cumcolSum==target):
                return True
        
        return False