class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if len(obstacleGrid)==0 :
            return 0

        m=len(obstacleGrid)-1
        n=len(obstacleGrid[0])-1

        dp=[]

        for i in range(0,m+1) :
            dp.append([0]*(n+1))

        i=m
        j=n

        while i>=0 :

            j=n
            while j>=0 :

                if i==m and j==n :
                    if obstacleGrid[i][j]==1 :
                        dp[i][j]=0
                    else :
                        dp[i][j]=1

                elif obstacleGrid[i][j]==1 :
                    dp[i][j]=0

                elif i==m :
                    dp[i][j]=dp[i][j+1]

                elif j==n :
                    dp[i][j]=dp[i+1][j]

                else :
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]

                j-=1
            i-=1


        return dp[0][0]





                    
