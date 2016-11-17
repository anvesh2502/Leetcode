class Solution(object):


    def searchLeft(self,nums,target,i=-1,j=-1) :

        if i==-1 and j==-1 :
            i=0
            j=len(nums)-1

        if i>j :
            return -1

        mid=(i+j)/2

        if nums[mid]==target :

            if mid==0 :
                return 0

            if nums[mid-1]!=target :
                return mid

            return self.searchLeft(nums,target,i,mid-1)

        if nums[mid]>target :
            return self.searchLeft(nums,target,i,mid-1)

        return self.searchLeft(nums,target,mid+1,j)


    def searchRight(self,nums,target,i=-1,j=-1) :

        if i==-1 and j==-1 :
            i=0
            j=len(nums)-1

        if i>j :
            return -1

        mid=(i+j)/2

        if nums[mid]==target :

            if mid==j :
                return j

            if nums[mid+1]!=target :
                return mid

            return self.searchRight(nums,target,mid+1,j)

        if nums[mid]>target :
            return self.searchRight(nums,target,i,mid-1)

        return self.searchRight(nums,target,mid+1,j)






    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i=self.searchLeft(nums,target)

        j=self.searchRight(nums,target)


        if i==-1 or j==-1 :
            return [-1,-1]

        return [i,j]    
