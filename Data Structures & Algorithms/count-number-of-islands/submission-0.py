class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        maxX = len(grid[0])
        maxY=len(grid)
        islands=0
        def explore(x,y): #to the right, then down
            if(0>x or x>=maxX):
                return
            if(0>y or y>=maxY):
                return
            if((x,y) in seen):
                return
            if(grid[y][x]=="0"):
                return
            elif(grid[y][x]=="1"):
                seen.add((x,y))
            explore(x+1,y)
            explore(x,y+1)
            explore(x-1,y)
            explore(x,y-1)
            
        for x in range(maxX):
            for y in range(maxY):
                if(grid[y][x]=="1" and (x,y) not in seen):
                    explore(x,y)
                    islands +=1
        return islands

