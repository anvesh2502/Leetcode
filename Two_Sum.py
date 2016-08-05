class Solution(object):
    def twoSum(self, nums, target):

       indices=dict()
       for i in range(0,len(nums)) :
            indices[nums[i]]=i

       for i in range(0,len(nums)) :

           if (target-nums[i]) in indices :
               i2=indices[target-nums[i]]
               if i!=i2 :
                   return [i,i2]





           
