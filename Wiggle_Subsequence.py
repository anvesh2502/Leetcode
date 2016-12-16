class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """




        if len(nums)==0 : return 0
        if len(nums)==1 : return 1

        l=[]

        for i in range(1,len(nums)) :
            if nums[i]==nums[i-1] : continue
            l.append(nums[i]-nums[i-1])


        if len(l)==0 : return 1


        i=len(l)-2
        dp=[1]*len(l)

        while i>=0 :

            j=i+1
            while j<len(l) :

                if l[i]<0 :
                    if l[j]>0 and dp[i]<1+dp[j] :
                        dp[i]=1+dp[j]


                elif l[i]>0 :
                    if l[j]<0 and dp[i]<1+dp[j] :
                        dp[i]=1+dp[j]

                j+=1
            i-=1

        return max(dp)+1

                
