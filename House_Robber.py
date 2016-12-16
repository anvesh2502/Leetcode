class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 : return 0

        dp=[0]*(len(nums))

        i=len(nums)-1

        while i>=0 :

            dp[i]=nums[i]
            j=i+2
            print i,j
            max_val=dp[i]
            while j<len(nums) :
                v=dp[i]+dp[j]
                if v>max_val :
                    max_val=v

                j+=1

            dp[i]=max_val

            i-=1


        print dp

        return max(dp)    
