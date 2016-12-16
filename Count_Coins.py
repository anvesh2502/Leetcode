class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount==0 :
            return 0

        dp=[99999]*(amount+1)
        dp[0]=0

        i=1
        while i<=amount :

            for coin in coins :

                if i==coin :
                    dp[i]=1

                if i>coin :
                    if dp[i-coin]==99999 or dp[coin]==99999 :
                        continue
                    else :
                        v=dp[i-coin]+dp[coin]
                        if v<dp[i] :
                            dp[i]=v



            i+=1


        if dp[amount]==99999 :
            return -1

        return dp[amount]














            
