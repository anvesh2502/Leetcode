class Solution(object):

    def isSquare(self,integer):
       root = math.sqrt(integer)
       if int(root + 0.5) ** 2 == integer:
        return True
       else:
        return False




    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if self.isSquare(n) : return 1

        dp=[0]*(n+1)
        i=1

        while i<=n :

           if self.isSquare(i) :
               dp[i]=1

           else :
               j=1
               min_total=n
               while j<i :

                  val=dp[j]+dp[i-j]
                  if min_total>val :
                      min_total=val
                  j+=1

               dp[i]=min_total

           i+=1

        return dp[n]
























        
