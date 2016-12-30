class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 : return 0

        if len(nums)==1 : return nums[0]

        dp=[]

        for i in range(0,len(nums)) :
            dp.append([0,0])


        i=len(nums)-1

        if nums[i]<0 :
            dp[i][1]=nums[i]

        else :
            dp[i][0]=nums[i]


        i-=1

        while i>=0 :

            if nums[i]>0 :

                if dp[i+1][0]!=0 :
                    dp[i][0]=nums[i]*dp[i+1][0]

                else :
                    dp[i][0]=nums[i]

                dp[i][1]=dp[i+1][1]*nums[i]

            else :

                if dp[i+1][1]!=0 :

                    dp[i][0]=dp[i+1][1]*nums[i]

                else :

                    dp[i][1]=nums[i]

                if dp[i+1][0]!=0 :
                    dp[i][1]=nums[i]*dp[i+1][0]

                else :
                    dp[i][1]=nums[i]








            i-=1




        max_val=-1

        for v in dp :
            if v[0]>max_val :
                max_val=v[0]

        print dp

        return max_val




















       
