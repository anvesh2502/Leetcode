class Solution(object):



    def permute(self,nums) :

        if len(nums)==1 : return (nums,)

        first=nums[0]
        nums=nums[1:]

        out=set()

        perms=self.permute(nums)

        for p in perms :

            for i in range(0,len(p)+1) :

                out.add(tuple(list(p[0:i])+[first]+list(p[i:])))


        return out




    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms=self.permute(nums)

        out=[]

        for p in perms :
            out.append(list(p))

        return out

















        
