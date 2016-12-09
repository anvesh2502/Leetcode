class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp=[]

        for i in range(0,m+1) :
            dp.append([0]*(n+1))

        i=m-1
        j=n-1

        while i>=0 :

            j=n-1
            while j>=0 :


                if i==m-1 and j==n-1 :
                    print i,j
                    dp[i][j]=1

                elif i==m-1 :
                    dp[i][j]=dp[i][j+1]

                elif j==n-1 :
                    dp[i][j]=dp[i+1][j]

                else :
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]

                j-=1

            i-=1


        return dp[0][0]












        
