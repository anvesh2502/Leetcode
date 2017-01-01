class Solution(object):

    def get_neighbors(self,grid,point) :

        x=point[0]
        y=point[1]
        neighbors=[]

        #East
        if (x-1)>=0  :
            neighbors.append((x-1,y))

        #West
        if (y+1)<=len(grid[0])-1 :
            neighbors.append((x,y+1))

        #North
        if (y-1)>=0 :
            neighbors.append((x,y-1))

        #South
        if (x+1)<=len(grid)-1 :
            neighbors.append((x+1,y))


        return neighbors








    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        queue=[]
        foundFlag=False
        current=(-1,-1)

        for i in range(0,len(grid)) :
            for j in range(0,len(grid[0])) :

                if grid[i][j]==1 :
                    current=(i,j)
                    foundFlag=True
                    break

            if foundFlag :
                break

        if current==(-1,-1) : return 0

        visited=set()
        perimeter=0
        queue=set()

        print current

        queue.add(current)


        while len(queue)!=0 :

            current=queue.pop()

            local_perimeter=0

            if current[0]==0 :
                local_perimeter+=1

            if current[0]==len(grid)-1 :
                local_perimeter+=1

            if current[1]==0 :
                local_perimeter+=1

            if current[1]==len(grid[0])-1 :
                local_perimeter+=1


            visited.add(current)

            neighbors=self.get_neighbors(grid,current)

            for neighbor in neighbors :

                if grid[neighbor[0]][neighbor[1]]==0 :
                    local_perimeter+=1

                elif neighbor not in visited :
                    queue.add(neighbor)


            perimeter+=local_perimeter





        return perimeter



        
