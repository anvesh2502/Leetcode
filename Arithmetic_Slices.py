class Solution(object):
    def numberOfArithmeticSlices(self, a):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(a)<3 : return 0

        dp=[0]*(len(a)+1)


        i=len(a)-3

        if (a[i]-a[i+1])==(a[i+1]-a[i+2]) :
            dp[i]=1

        while i>=0 :

            if (a[i]-a[i+1])==(a[i+1]-a[i+2]) :
                dp[i]=dp[i+1]+1

            else :
               dp[i]=0

            i-=1


        return sum(dp)


        
