class Solution(object):


    def get_rotation_index(self,a,low,high) :


        if low>high :
            return -1

        mid=(low+high)/2

        if mid==0 :
            return self.get_rotation_index(a,mid+1,high)

        if a[mid-1]>a[mid] and a[0]>a[mid] :
            return mid

        if a[mid-1]<a[mid] and a[0]<a[mid] :
            return self.get_rotation_index(a,mid+1,high)

        return self.get_rotation_index(a,low,mid-1)


    def binary_search(self,a,low,high,val) :

        if low>high :
            return -1

        mid=(low+high)/2

        if a[mid]==val :
            return mid


        if a[mid]>val :
            return self.binary_search(a,low,mid-1,val)


        return self.binary_search(a,mid+1,high,val)



    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        div=self.get_rotation_index(nums,0,len(nums)-1)


        if div==-1 :
            return self.binary_search(nums,0,len(nums)-1,target)

        if div==0 :
            if nums[0]==target :
                return 0

            return self.binary_search(nums,1,len(nums)-1,target)

        if target>=nums[0] and target<=nums[div-1] :
            return self.binary_search(nums,0,div-1,target)

        return self.binary_search(nums,div,len(nums)-1,target)
