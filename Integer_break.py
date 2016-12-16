class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 : return 0
        if n==1 : return 1

        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1


        i=0

        for i in range(2,n+1) :

            max_val=-1
            for j in range(1,i) :

                v=dp[j]*dp[i-j]

                if v>max_val :
                    max_val=v


                product1=j*(i-j)
                product2=dp[j]*(i-j)
                product3=j*dp[i-j]

                product=max(product1,product2,product3)




                if max_val < product :
                    max_val=product



            dp[i]=max_val



        return dp[n]

        
