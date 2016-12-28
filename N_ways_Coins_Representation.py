
def coinWays(n,coins) :

    dp=[0]*(n+1)

    dp[0]=1

    for i in range(1,n+1) :
        for coin in coins :

            if coin<=i :
                dp[i]+=dp[i-coin]*dp[coin]


    return dp[n]

print coinWays(200,[1,5,10,25])                
