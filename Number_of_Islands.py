class Solution(object):


    def get_neighbors(self,grid,point) :


        x=point[0]
        y=point[1]

        neighbors=[]

        if x>0 and grid[x-1][y]=='1':
            neighbors.append((x-1,y))

        if x<len(grid)-1 and grid[x+1][y]=='1':
            neighbors.append((x+1,y))

        if y>0 and grid[x][y-1]=='1':
            neighbors.append((x,y-1))

        if y<len(grid[0])-1 and grid[x][y+1]=='1':
            neighbors.append((x,y+1))

        return neighbors


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands=[]
        foundFlag=False
        visited=set()
        island_count=0

        for i in range(0,len(grid)) :
            for j in range(0,len(grid[0])) :

                if grid[i][j]=='1' and (i,j) not in visited :

                    current=(i,j)

                    queue=[]
                    queue.append(current)


                    while len(queue)!=0 :

                      current=queue.pop()
                      visited.add(current)

                      if current in islands :
                       islands.remove(current)

                      neighbors=self.get_neighbors(grid,current)

                      for neighbor in neighbors :

                       if neighbor in visited :
                        continue

                       queue.append(neighbor)



                    island_count+=1



        return island_count





















        
