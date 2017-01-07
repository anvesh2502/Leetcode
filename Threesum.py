class Solution(object):


    def exists(self,nums,val,start,end) :

        if start>end :
            return False

        if start==end :
            if nums[start]==val : return True
            return False

        mid=(start+end)/2

        if nums[mid]==val : return True

        if nums[mid]>val :
            return self.exists(nums,val,start,mid-1)

        return self.exists(nums,val,mid+1,end)





    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums)==0 : return []

        nums.sort()
        pairs=set()
        out=[]
        end=len(nums)-1

        for i in range(0,len(nums)-1) :
            for j in range(i+1,len(nums)) :
                rem=-1*(nums[i]+nums[j])

                if (nums[i],nums[j]) in pairs :
                    continue
                else :
                 if self.exists(nums,rem,j+1,end) :
                    out.append([nums[i],nums[j],rem])
                    pairs.add((nums[i],nums[j]))




        return out







        
