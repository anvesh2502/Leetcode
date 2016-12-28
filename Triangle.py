class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp=[]

        for l in triangle :
            dp.append([999]*len(l))


        for i in range(0,len(triangle[-1])) :

            dp[-1][i]=triangle[-1][i]


        i=len(triangle)-2
        j=0

        while i>=0 :

            j=0
            while j<len(dp[i]) :

                dp[i][j]=triangle[i][j]+min(dp[i+1][j+1],dp[i+1][j])

                j+=1

            i-=1


        return dp[0][0]

        
