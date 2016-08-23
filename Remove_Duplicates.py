class Solution(object):
    def removeDuplicates(self, nums):

       if len(nums)==0 :
           return 0

       s=0
       f=1

       while f<len(nums) :

           if nums[f-1]!=nums[f] :
               nums[s+1]=nums[f]
               s+=1
           f+=1

       return s+1

       
