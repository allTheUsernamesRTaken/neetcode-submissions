class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxX=len(grid[0])
        maxY=len(grid)
        maxArea = 0
        def explore(startx,starty):
            cur = 0
            stack = [(startx,starty)]
            while(len(stack)>0):
                #print(stack)
                x,y = stack.pop()
                cur+=1
                a,b,c,d = (x+1,y),(x,y+1),(x-1,y),(x,y-1)
                for adj in [a,b,c,d]:
                    xA,yA=adj[0],adj[1]
                    if(maxX>xA>=0 and maxY>yA>=0):#valid coord
                        if(grid[yA][xA]==1): #neighbor = 1
                            if((xA,yA) not in seen): #not explored
                                stack.append((xA,yA))
                                seen.add((xA,yA))
            return cur
        for x in range(maxX):
            for y in range(maxY):
                if((x,y) not in seen and grid[y][x]==1):
                    #print("new island")
                    seen.add((x,y))
                    maxArea=max(explore(x,y),maxArea)
        return maxArea
        



