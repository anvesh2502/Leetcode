class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d=dict()
        i=0
        while i<len(nums) :
            d.setdefault(nums[i],[])
            d[nums[i]].append(i+1)
            i+=1

        nums.sort()
        i=0
        j=len(nums)-1

        while i<j :
            total=nums[i]+nums[j]
            if total==target :
                if nums[i]==nums[j] :
                  return [d[nums[i]][0],d[nums[i]][1]]
                else :
                 return [d[nums[i]][0],d[nums[j]][0]]

            elif total>target :
                j-=1
            else :
                i+=1

        return None
