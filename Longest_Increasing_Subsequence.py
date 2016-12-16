class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0 : return 0

        dp=[]

        for v in nums :
            dp.append(1)

        length=1

        i=len(nums)-2

        while i>=0 :

            j=i+1
            while j<len(nums) :
                if nums[i]<nums[j] and dp[i]<dp[j]+1 :
                    dp[i]=dp[j]+1

                j+=1

            i-=1

        return max(dp)




        
