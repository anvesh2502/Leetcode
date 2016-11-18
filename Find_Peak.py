class Solution(object):
    def findPeakElement(self, nums,low=-1,high=-1):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==1 :
            return 0

        if low==-1 and high==-1 :
            low=0
            high=len(nums)-1

        if low>high :
            return -1

        mid=(low+high)/2

        if mid==0 :
            if nums[mid]>nums[mid+1] :
                return mid

            return self.findPeakElement(nums,mid+1,high)

        if mid==high :
            if nums[mid-1]<nums[mid] :
                return mid

            return self.findPeakElement(nums,low,mid-1)

        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1] :
            return mid

        if nums[mid+1]>nums[mid] :
            return self.findPeakElement(nums,mid+1,high)

        return self.findPeakElement(nums,low,mid-1)





        
