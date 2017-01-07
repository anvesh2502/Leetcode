class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """



        if len(nums)==0 :
            return [[]]


        if len(nums)==1 :
            return [[nums[0]],[]]


        out_list=[]


        #out_list.append([nums[0]])

        start=nums[0]
        nums=nums[1:]

        small_list=self.subsets(nums)

        for li in small_list :

            out_list.append([start]+li)
            out_list.append(li)


        return out_list


















            
