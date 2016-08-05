class Solution(object):
    def missingNumber(self, nums):

        total=sum(nums)
        n=len(nums)
        maximum=n*(n+1)/2
        return maximum-total

        
