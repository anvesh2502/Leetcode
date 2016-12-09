class Solution(object):
    def minPathSum(self, cost):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[]

        if len(cost)==0 :
            return 0


        for i in range(0,len(cost)) :
          dp.append([0]*len(cost[0]))

        i=len(cost)-1
        j=len(cost[0])-1

        while i>=0 :

         j=len(cost[0])-1
         while j>=0 :

          if i==len(cost)-1 and j==len(cost[0])-1 :
           dp[i][j]=cost[i][j]

          elif i==len(cost)-1 :
           dp[i][j]=cost[i][j]+dp[i][j+1]

          elif j==len(cost[0])-1 :
           dp[i][j]=cost[i][j]+dp[i+1][j]

          else :
           dp[i][j]=cost[i][j]+min(dp[i+1][j],dp[i][j+1])

          j-=1

         i-=1

        return dp[0][0]
